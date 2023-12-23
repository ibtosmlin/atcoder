import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

def prod(ma, mb, mod=1):
    h_a = len(ma)
    w_a = len(ma[0])
    h_b = len(mb)
    w_b = len(mb[0])
    if h_a*w_a*h_b*w_b == 0: return 0
    if w_a != h_b: return 0
    ret = [[0] * h_a for _ in range(w_b)]
    for i in range(h_a):
        for j in range(w_b):
            c = 0
            for k in range(w_a):
                c += ma[i][k]*mb[k][j]
                c %= mod
            ret[i][j] = c
    return ret


def powmat(ma, k, mod = 10**9+7):
    n = len(ma)
    ret = [[0]*n for _ in range(n)]
    for i in range(n):
        ret[i][i] = 1
    for _ in range(k):
        if k & 1:
            ret = prod(ret, ma, mod)
        ma = prod(ma, ma, mod)
        k >>= 1
        if k == 0: break
    return ret

N, K = map(int, input().split())
ma = [list(map(int, input().split())) for _ in range(N)]

ret = powmat(ma, K, 998244353)
for r in ret:
    print(*r)
