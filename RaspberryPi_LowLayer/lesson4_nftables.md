# Lesson 4: nftables で捨てる

## ゴール

「どこで見えて、どこで見えなくなるか」が分かる。

## 背景

`tcpdump`（や Lesson 3 の `AF_PACKET` ソケット）は、Netfilter より手前でパケットを見る、パケットタップと呼ばれる仕組み。そのため、nftables で `drop` されたパケットも、タップ側には見え続ける。

一方、ソケットの `recv_from()`（つまり通常のアプリケーション）は、Netfilter を通過した後にしかパケットを受け取れない。nftables で `drop` すれば、アプリには届かなくなる。

この「見える場所」と「見えなくなる場所」の違いが、参考記事の「どこで捨てるか」という話の土台になる。

Netfilterのhookの位置は、`prerouting → input / forward → output → postrouting` という流れになっている。nftablesは独立した層ではなく、このhook上に設置するルール、という理解で良い。

## 実験

### 1. ルールを入れる前の状態を確認する

```bash
# ターミナル1（タップ）
sudo tcpdump -i eth0 -n udp port 4000

# ターミナル2（アプリ側、Lesson 3のスクリプトでも、ncでも良い）
sudo python3 scripts/eth_udp_parser.py eth0
```

別の端末から `nc -u <PiのIPアドレス> 4000` で送って、両方に届くことを確認する。

### 2. nftables でルールを入れる

```bash
sudo nft add table inet filter
sudo nft add chain inet filter input { type filter hook input priority 0 \; }
sudo nft add rule inet filter input udp dport 4000 drop
```

もう一度送信して、以下を確認する。

- `tcpdump` には**見える**（Netfilterより手前なので）
- Lesson 3 のPythonスクリプト（`AF_PACKET`）にも**見える**（同じ理由）
- 通常のUDPソケットで受信するアプリ（例えば `nc -u -l 4000` で待ち受けたもの）には**届かない**

### 3. 片付け

```bash
sudo nft flush chain inet filter input
sudo nft delete chain inet filter input
sudo nft delete table inet filter
```

ルールを入れたままにしないよう、実験が終わったら必ず消す。

## セキュリティ面の注意

- nftables のルールを操作するには root 権限が必要。ルールの消し忘れは、自分でも気づかないうちに通信を止め続ける原因になる
- ルールを消す処理が失敗した場合に気づけるよう、スクリプト化するときはエラーを握りつぶさずログを出す。`SIGKILL` や電源断ではクリーンアップ処理自体が走らないので、起動時に残骸を掃除する処理も検討する

## 自分の言葉で説明してみる

- `tcpdump` には見えるのに、アプリには届かない、という状態がなぜ起きるのか
- Netfilterのhookの並び（prerouting → input/forward → output → postrouting）のうち、今回使った `input` hookはどの役割か
- 自分の実験結果（何が見えて、何が見えなくなったか）

<!-- 実行結果・分からなかった点をここに書き足していく -->
