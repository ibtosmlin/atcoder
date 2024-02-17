# https://atcoder.jp/contests/abc341/tasks/abc341_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
n = int(input())
a = list(map(int, input().split()))
now = a[0]
for i in range(1, n):
    s, t = map(int, input().split())
    now = now // s * t + a[i]
print(now)