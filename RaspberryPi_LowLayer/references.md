# 参考資料

段階別にまとめた。Lesson 0〜5 の順番と対応させている。

版や在庫、最新情報は購入・利用前に確認すること。GitHubのチュートリアルやブログのコードは、中身を読まずに `sudo` で実行しないこと。

## ① 土台: TCP/IP とヘッダ構造（Lesson 0〜2 向け）

- 『マスタリングTCP/IP 入門編』（オーム社） — 定番書。Ethernet、IP、UDPのヘッダ構造を学べる
- 『ネットワークはなぜつながるのか』（日経BP） — パケットが実際にどう旅するかを図で理解できる

## ② Linuxから見たネットワークとカーネル（Lesson 3〜4 向け）

- 『[試して理解]Linuxのしくみ』（技術評論社、武内覚） — 実験しながらOSの基礎が学べる。カーネルとユーザー空間の関係、プロセスとシステムコールの理解に役立つ
- 『詳解UNIXネットワークプログラミング』 — ソケットの理解を深めたいときに、必要な章をつまみ読みする
- [Beej's Guide to Network Programming](https://beej.us/guide/bgnet/)（無料、英語） — ソケットプログラミングの入門

## ③ パケットの受信経路（Lesson 4〜5 向け、記事に直結）

- packagecloud "Monitoring and Tuning the Linux Networking Stack: Receiving Data"（英語） — NICからソケットまでの受信経路を、カーネルのコードを辿りながら解説した記事
- Netfilter / nftables wiki の packet flow 図 — hookの通過順序を一枚で確認できる
- [nftables公式wiki](https://wiki.nftables.org/) — ルールの書き方とhookの位置関係

## ④ eBPF / XDP（Lesson 5 より先）

- 『入門 eBPF ―Linuxカーネルの可視化と機能拡張』（オライリー・ジャパン、2023年12月） — 日本語で読めるeBPFの入門書
- [xdp-project/xdp-tutorial](https://github.com/xdp-project/xdp-tutorial)（GitHub） — 手を動かして学べる公式チュートリアル。Generic/Nativeの違いも扱う
- BCC / bpftrace のドキュメント — PythonからeBPFに触りたい場合の入口

## ⑤ Python側のツール

- [Scapy](https://scapy.net/) 公式ドキュメント — パケットの組み立て・送信・解析
- Python標準ライブラリ `socket` / `struct` のドキュメント — Lesson 3 のスクリプトの土台

## おすすめの進め方

1. ①でヘッダ構造を理解し、Lesson 2〜3のコードの各バイト位置の意味を説明できるようにする
2. 手元で `tcpdump` と自作パーサの出力を見比べる（Lesson 1〜3）
3. ③の記事で受信経路を追い、nftablesを使った実験を行う（Lesson 4）
4. 記事（Lesson 5）を理解する
5. 最後に④でeBPF/XDPに進む
