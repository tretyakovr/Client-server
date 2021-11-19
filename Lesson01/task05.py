"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из
байтовового в строковый тип на кириллице.
"""

import subprocess

ping_count = 10
cmd = ['ping', '-c', str(ping_count)]
hosts = ['yandex.ru', 'youtube.com']

for host in hosts:
    args = cmd.copy()
    args.append(host)
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

    print(*args)
    for line in subproc_ping.stdout:
        print(line.decode('utf-8'), end='')

    print('\n')

# На счет кириллицы - ? у меня MacOS
# result:
# ping -c 10 yandex.ru
# PING yandex.ru (5.255.255.88): 56 data bytes
# 64 bytes from 5.255.255.88: icmp_seq=0 ttl=55 time=113.602 ms
# 64 bytes from 5.255.255.88: icmp_seq=1 ttl=55 time=113.221 ms
# 64 bytes from 5.255.255.88: icmp_seq=2 ttl=55 time=165.513 ms
# 64 bytes from 5.255.255.88: icmp_seq=3 ttl=55 time=113.091 ms
# 64 bytes from 5.255.255.88: icmp_seq=4 ttl=55 time=113.060 ms
# 64 bytes from 5.255.255.88: icmp_seq=5 ttl=55 time=112.899 ms
# 64 bytes from 5.255.255.88: icmp_seq=6 ttl=55 time=113.410 ms
# 64 bytes from 5.255.255.88: icmp_seq=7 ttl=55 time=112.072 ms
# 64 bytes from 5.255.255.88: icmp_seq=8 ttl=55 time=112.984 ms
# 64 bytes from 5.255.255.88: icmp_seq=9 ttl=55 time=113.637 ms
#
# --- yandex.ru ping statistics ---
# 10 packets transmitted, 10 packets received, 0.0% packet loss
# round-trip min/avg/max/stddev = 112.072/118.349/165.513/15.727 ms
#
#
# ping -c 10 youtube.com
# PING youtube.com (64.233.165.136): 56 data bytes
# 64 bytes from 64.233.165.136: icmp_seq=0 ttl=107 time=195.492 ms
# 64 bytes from 64.233.165.136: icmp_seq=1 ttl=107 time=216.017 ms
# 64 bytes from 64.233.165.136: icmp_seq=2 ttl=107 time=136.203 ms
# 64 bytes from 64.233.165.136: icmp_seq=3 ttl=107 time=155.833 ms
# 64 bytes from 64.233.165.136: icmp_seq=4 ttl=107 time=180.486 ms
# 64 bytes from 64.233.165.136: icmp_seq=5 ttl=107 time=200.890 ms
# 64 bytes from 64.233.165.136: icmp_seq=6 ttl=107 time=223.033 ms
# 64 bytes from 64.233.165.136: icmp_seq=7 ttl=107 time=128.893 ms
# 64 bytes from 64.233.165.136: icmp_seq=8 ttl=107 time=168.150 ms
# 64 bytes from 64.233.165.136: icmp_seq=9 ttl=107 time=187.059 ms
#
# --- youtube.com ping statistics ---
# 10 packets transmitted, 10 packets received, 0.0% packet loss
# round-trip min/avg/max/stddev = 128.893/179.206/223.033/30.206 ms
