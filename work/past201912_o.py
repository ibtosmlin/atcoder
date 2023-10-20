# https://atcoder.jp/contests/past201912-open/tasks/past201912_o
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1
def fstr(x): return f'{x:.14f}'

n = int(input())
A = [None] * n
S = set([0])
for i in range(n):
    ai = sorted(map(int, input().split()))
    A[i] = ai
    for si in ai:
        S.add(si)
d = {si: i for i, si in enumerate(sorted(S))}
N = len(d)
p = dict()
for i in range(n):
    for j in range(6):
        A[i][j] = d[A[i][j]]
        p[A[i][j]] = i

dp = [0] * N
# jのダイスを選ぶ時の期待値
ev = [1] * n
mev = 1
# dp[i]: iの状態でjのダイスを選ぶ時の期待値
for j in range(n):
    dp[N-1] = 1

for i in range(N-1)[::-1]:
    u = 0
    ev[p[i+1]] += dp[i+1] / 6
    mev = max(mev, ev[p[i+1]])
    dp[i] = mev

print(fstr(dp[0]))
