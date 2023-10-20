# https://atcoder.jp/contests/abc220/tasks/abc220_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

mod = 998244353
n, d = map(int, input().split())

pow2 = [1]
for i in range(100100):
    pow2.append(pow2[-1] * 2 % mod)

def cntd(l):
    # lのノードから下にある
    # dのノード     pow(2, d)個　(l+d<n)
    if l+d< n: return pow2[d]
    return 0

def cntu(l):
    # L = l + d - 2 * i
    # L > l :  l+d > 2*i
    # pow2[L] - pow2[L-l]
    # L <= l : pow2[L] - 1
    ret = 0
    for i in range(1, d+l):
        L = l + d - 2 * i
        if L < 0: break
        if L <= l:
            ret += pow2[L] - 1
        else:
            ret += pow2[L] - pow2[L-l]
    return ret

ret = 0
for l in range(n):
    ret += (cntd(l) + cntu(l))* pow2[l] % mod
    ret %= mod
print(ret)
#print(ret * pow(2, mod-2, mod) % mod)
