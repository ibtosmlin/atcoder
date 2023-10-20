# https://atcoder.jp/contests/past201912-open/tasks/past201912_n
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from collections import defaultdict

n, w, c = map(int, input().split())
INF = 10**18

pos = set([0, w-c])
event = defaultdict(int)
for _ in range(n):
    l, r, p = map(int, input().split())
    event[max(l - c + 1, 0)] += p
    event[r] -= p

event[0] += 0
event[w-c] += 0

ret = INF
now = 0
for x in sorted(event.keys()):
    if x > w-c: break
    now += event[x]
    ret = min(now, ret)
print(ret)
