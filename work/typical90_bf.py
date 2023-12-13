# https://atcoder.jp/contests/typical90/tasks/typical90_bf
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

maxdeg = 100
N = 100000
n, k = map(int, input().split())

def f(i):
    ret = i
    while i:
        ret += i%10
        i //= 10
    # 1回の遷移
    return ret % 100000


def doubbling():
    dp = [[0] * N for _ in range(maxdeg)]
    for i in range(N):
        dp[0][i] = f(i)

    for t in range(1, maxdeg):
        for i in range(N):
            dp[t][i] = dp[t-1][dp[t-1][i]]
    return dp

dp = doubbling()

def fk(i, k):
    # iからk回遷移した時の結果
    for d in range(maxdeg):
        if k >> d & 1: i = dp[d][i]
    return i

print(fk(n, k))
