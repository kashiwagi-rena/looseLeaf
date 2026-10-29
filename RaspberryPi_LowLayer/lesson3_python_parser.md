# Lesson 3: Python で同じことをする

## ゴール

自作パーサが tcpdump の出力と一致する。

## スクリプト

[`scripts/eth_udp_parser.py`](./scripts/eth_udp_parser.py) に、Ethernet + IPv4 + UDP の最小パーサを置いた。

元になったコードは以下（会話で最初に出てきたバージョン）。

```python
import socket, struct

ETH_P_ALL = 0x0003
s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_ALL))

while True:
    frame, _ = s.recvfrom(65535)
    dst, src, eth_type = struct.unpack("!6s6sH", frame[:14])
    if eth_type != 0x0800:  # IPv4 以外は今回は無視
        continue

    ihl = (frame[14] & 0x0F) * 4  # IPヘッダ長。固定の20にしない
    proto = frame[23]
    src_ip = socket.inet_ntoa(frame[26:30])
    dst_ip = socket.inet_ntoa(frame[30:34])

    if proto == 17:  # UDP
        l4 = 14 + ihl
        sport, dport = struct.unpack("!HH", frame[l4:l4 + 4])
        print(f"UDP {src_ip}:{sport} -> {dst_ip}:{dport}")
```

このコードには1つ弱点がある。`frame[l4:l4+4]` などのスライスは、`frame` がその長さに達していなくても例外を出さず、短いバイト列を返す。すると `struct.unpack` の方で長さ不足のエラーが起きる。細工された（あるいは壊れた）短いパケットが来ると落ちる。

`scripts/eth_udp_parser.py` では、各ヘッダを読む前に `len(frame)` が十分かを確認してから読むようにしている。この「読む前に長さを確認する」が、低レイヤーのコードを書く上での基本の作法になる。

## 実験

### 1. 動かしてみる

```bash
sudo python3 scripts/eth_udp_parser.py eth0
```

別の端末から UDP を送る。

```bash
echo "hello" | nc -u <PiのIPアドレス> 4000
```

### 2. tcpdump と見比べる

ターミナルを2つ使い、同じタイミングで両方を動かして、同じ送信元/宛先IP・ポート番号が出ることを確認する。

```bash
# ターミナル1
sudo python3 scripts/eth_udp_parser.py eth0

# ターミナル2
sudo tcpdump -i eth0 -n udp
```

### 3. 壊れたパケットで確認する（任意）

元のコード（長さチェックなし）と、`scripts/eth_udp_parser.py`（長さチェックあり）を比べて、どちらが短いパケットに対して安全かを考える。実際に短いUDPパケットを作って試す場合は、自分のネットワーク内だけで行う。

## セキュリティ面の注意

- raw socket は強い権限（root）が必要。実験コードに外部からの入力をそのまま処理させるとリスクが上がるので、受け取ったバイト列は信用せず、長さのチェックを必ず行う
- `sudo python` を常用する癖をつけない。学習用なら構わないが、本番では `CAP_NET_RAW` だけを付与する形にする

## 自分の言葉で説明してみる

- なぜ `ihl` を `20` に固定してはいけないのか
- 長さチェックを入れないと、どんな入力でクラッシュするか
- 自分の実行結果（tcpdumpと一致したか、しなかった場合は何が違ったか）

<!-- 実行結果・分からなかった点をここに書き足していく -->
