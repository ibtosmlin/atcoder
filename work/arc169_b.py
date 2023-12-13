# https://atcoder.jp/contests/arc169/tasks/arc169_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n, s = map(int, input().split())
A = list(map(int, input().split()))

P = [None] * n
pi = 0
sm = 0
for i in range(n):
    while pi < n and sm + A[pi] <= s:
        sm += A[pi]
        pi += 1
    P[i] = pi
    pi -= 1
    sm -= A[i] + A[pi]

ret = 0
dp = [0] * (n+1)
for i in range(n)[::-1]:
    dp[i] = dp[P[i]] + n - i
    ret += dp[i]
print(ret)
