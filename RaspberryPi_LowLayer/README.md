# Raspberry Pi で低レイヤーをキャッチアップする

Raspberry Pi と Python を使って、パケットがネットワークインターフェースに届いてからアプリケーションに渡るまでの「低レイヤーの情報の流れ」を、実際に手を動かして確認していくカリキュラムです。

## きっかけ

以下の記事を読んで、「どこでパケットを捨てるか」によって処理負荷が変わる、という実験に興味を持ったのが出発点です。

- [ぱけっとぽいぽい（Qiita）](https://qiita.com/Suisan-neki/items/cafab8fd958a80ab10ee) — Rust + Raspberry Pi 2台で、XDP / nftables / ユーザー空間のそれぞれでUDPパケットを破棄した場合のCPU負荷を比較した実験

この記事を自分の言葉で説明できるようになることを、ひとまずのゴールに置いています（Lesson 5）。

## 全体ロードマップ

| 回 | テーマ | ゴール |
|---|---|---|
| [Lesson 0](./lesson0_envelope.md) | 通信は封筒の入れ子 | Ethernet / IP / UDP(TCP) / アプリデータの4層を、封筒の例えで説明できる |
| [Lesson 1](./lesson1_tcpdump.md) | tcpdump で実物を見る | 流れているパケットを観察できる |
| [Lesson 2](./lesson2_hex_header.md) | ヘッダを手で読む | 16進数のダンプから IP アドレスなどを読める |
| [Lesson 3](./lesson3_python_parser.md) | Python で同じことをする | 自作パーサが tcpdump の出力と一致する |
| [Lesson 4](./lesson4_nftables.md) | nftables で捨てる | 「どこで見えて、どこで見えなくなるか」が分かる |
| [Lesson 5](./lesson5_article_analysis.md) | 記事の実験を理解する | 「ぱけっとぽいぽい」を自分の言葉で説明できる |

Lesson 5 より先（XDP / eBPF を実際に書く話）は、必要になった時点で追加する。

## 用意するもの

- Raspberry Pi 1台（有線LAN推奨。無線でも可）
- パケットを送る側になる別のPCやスマホ（同じLAN内）
- Python3（Raspberry Pi OS には標準で入っている）
- `tcpdump`（入っていなければ `sudo apt install tcpdump`）
- `nftables`（Lesson 4 から。入っていなければ `sudo apt install nftables`）

## 進め方

1. 各 Lesson の指示に従って、Raspberry Pi 上で実験する
2. 「自分の言葉で説明してみる」の問いに、自分なりの答えをその Lesson のファイルに書き足していく
3. 詰まったところや疑問点もそのまま書き足す（あとで見返す材料になる）

## セキュリティ上の注意（共通）

- `tcpdump` や raw socket は、自分が管理しているネットワークの中だけで使う。他人の通信を覗くと法的・倫理的な問題になる
- 学習メモには自宅のネットワーク構成（IPアドレス、MACアドレスなど）が自然と混ざる。この手の情報をコミットするときは、MACアドレスの後半など一部を伏せる
- `sudo` が必要なコマンドは、内容を理解してから実行する。ネットで拾ったスクリプトをそのまま `sudo` で実行しない
- APIキーやパスワード、SSH秘密鍵は絶対にコミットしない（一度 push すると履歴に残り続ける）

## 参考資料

段階別の参考書籍・記事は [references.md](./references.md) にまとめた。
