# https://atcoder.jp/contests/abc319/tasks/abc319_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
m = 840
n, x, y = map(int, input().split())
bus = [tuple(map(int, input().split())) for _ in range(n-1)]
d = [None] * m
for i in range(m):
    s = i
    s += x
    for p, t in bus:
        s += (p - s%p)%p + t
    s += y
    d[i] = s

for _ in range(int(input())):
    qi = int(input())
    print(d[qi%m] + m * (qi//m))
