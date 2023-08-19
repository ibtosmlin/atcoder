# https://atcoder.jp/contests/past201912-open/tasks/past201912_o
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1
from bisect import bisect_right

INF = 10**10
n = int(input())
dices = [sorted(map(int, input().split())) for _ in range(n)]

vals = set()
for dice in dices:
    for v in dice:
        vals.add(v)
vals.add(INF)
vals = sorted(vals)
vpos = {v:i for i, v in enumerate(vals)}
N = len(vals)
dp = [0] * N

for i in range(N):
    now = vals[i]
    for j in range(n):
        x = dices[j]
        next = 6 - bisect_right(x, now)
