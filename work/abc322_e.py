# https://atcoder.jp/contests/abc322/tasks/abc322_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from collections import defaultdict
n, k, p = map(int, input().split())
P = p+1

INF = 10 ** 18

dp = defaultdict(lambda: INF)
dp[0] = 0

def plist(x):
    ret = []
    for i in range(k):
        ret.append(x%P)
        x //= P
    return ret

def pnum(l):
    ret = 0
    for li in l[::-1]:
        ret *= P
        ret += li
    return ret

for _ in range(n):
    c, *A = map(int, input().split())
    ndp = defaultdict(lambda: INF)
    for s, v in dp.items():
        ndp[s] = min(ndp[s], v)
        pl = plist(s)
        for i, ai in enumerate(A):
            pl[i] = min(p, pl[i] + ai)
        ns = pnum(pl)
        ndp[ns] = min(ndp[ns], v + c)
    dp = ndp


ret = dp[pnum([p]*k)]
print(-1 if ret == INF else ret)
