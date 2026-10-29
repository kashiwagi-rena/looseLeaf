"""
Ethernet + IPv4 + UDP の最小パーサ。

Lesson 3 用のサンプル。root権限(sudo)で実行する必要がある。
tcpdump -n -e の出力と、このスクリプトの出力が一致するかを確認するのが目的。

実行例:
    sudo python3 eth_udp_parser.py eth0
"""

import socket
import struct
import sys

ETH_P_ALL = 0x0003
ETH_HEADER_LEN = 14
IPV4_ETHERTYPE = 0x0800
UDP_PROTOCOL = 17


def parse_ethernet(frame: bytes):
    if len(frame) < ETH_HEADER_LEN:
        return None
    dst, src, eth_type = struct.unpack("!6s6sH", frame[:ETH_HEADER_LEN])
    return {
        "dst_mac": dst.hex(":"),
        "src_mac": src.hex(":"),
        "eth_type": eth_type,
    }


def parse_ipv4(frame: bytes):
    # IPヘッダの先頭1バイト(version+ihl)が読めるだけの最小長を確認する
    if len(frame) < ETH_HEADER_LEN + 1:
        return None

    version_ihl = frame[ETH_HEADER_LEN]
    ihl = (version_ihl & 0x0F) * 4
    ip_header_end = ETH_HEADER_LEN + ihl

    # IHL分のIPヘッダが実際に全部届いているかを確認する
    if ihl < 20 or len(frame) < ip_header_end:
        return None

    proto = frame[ETH_HEADER_LEN + 9]
    src_ip = socket.inet_ntoa(frame[ETH_HEADER_LEN + 12 : ETH_HEADER_LEN + 16])
    dst_ip = socket.inet_ntoa(frame[ETH_HEADER_LEN + 16 : ETH_HEADER_LEN + 20])

    return {
        "ihl": ihl,
        "proto": proto,
        "src_ip": src_ip,
        "dst_ip": dst_ip,
        "header_end": ip_header_end,
    }


def parse_udp(frame: bytes, ip_header_end: int):
    udp_header_end = ip_header_end + 8
    if len(frame) < udp_header_end:
        return None

    sport, dport = struct.unpack("!HH", frame[ip_header_end : ip_header_end + 4])
    return {"sport": sport, "dport": dport}


def main():
    if len(sys.argv) != 2:
        print(f"usage: sudo python3 {sys.argv[0]} <interface>", file=sys.stderr)
        sys.exit(1)

    iface = sys.argv[1]
    s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(ETH_P_ALL))
    s.bind((iface, 0))

    print(f"listening on {iface} ... (Ctrl+C to stop)")
    while True:
        frame, _ = s.recvfrom(65535)

        eth = parse_ethernet(frame)
        if eth is None or eth["eth_type"] != IPV4_ETHERTYPE:
            continue

        ip = parse_ipv4(frame)
        if ip is None or ip["proto"] != UDP_PROTOCOL:
            continue

        udp = parse_udp(frame, ip["header_end"])
        if udp is None:
            continue

        print(
            f"UDP {ip['src_ip']}:{udp['sport']} -> {ip['dst_ip']}:{udp['dport']} "
            f"(eth {eth['src_mac']} -> {eth['dst_mac']})"
        )


if __name__ == "__main__":
    main()
