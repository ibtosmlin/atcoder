# https://atcoder.jp/contests/abc328/tasks/abc328_g
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000)
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

def popcount(x):
    ret = 0
    while x:
        ret += x%2
        x //= 2
    return ret

N, C = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
INF = -1

"""dp[s]: sまで使って一番右がiの場合の最小値"""
dp = [INF for _ in range(1<<N)]
dp[0] = 0

for s in range(1<<N):
    p = popcount(s)
    if dp[s] == -1: continue
    for l in range(N):
        if s >> l & 1: continue
        now = 0
        for r in range(l, N):
            if s >> r & 1: break
            now += abs(A[r] - B[p+r-l])
            t = s | ((1<<(r-l+1)) - 1 << l)
            nv = dp[s] + now + C
            if dp[t] == -1 or dp[t] > nv:
                dp[t] = nv
print(dp[-1]-C)