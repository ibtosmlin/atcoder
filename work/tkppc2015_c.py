# https://atcoder.jp/contests/tkppc/tasks/tkppc2015_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
def int1(x): return int(x)-1

n, m = map(int, input().split())
s = int(input())
eve = []
for _ in range(n):
    t, k = map(int, input().split())
    eve.append((t, k))
eve.append((s, 0))
eve.append((0, 0))
eve.sort()

ret = 0
N = len(eve)
nm = 0
for i in range(N-1):
    t, k = eve[i]
    nm += k
    if nm >= m:
        ret += eve[i+1][0] - t
print(ret)

