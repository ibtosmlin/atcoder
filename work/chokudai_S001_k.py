# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_k
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

mod = 1000000007
fac = [1]
for i in range(1, 100000):
    fac.append(fac[-1]*i%mod)

class BIT:
    def __init__(self, size):
        self.size = size; self.dat = [0]*(size+1)

    def update(self, i, x):
        i += 1
        while i <= self.size: self.dat[i] = x; i += i & -i

    def sum(self, r):
        r += 1; s = 0
        while r: s += self.dat[r];r -= r & -r
        return s

##################################

n = int(input())
a = list(map(int1, input().split()))
bit = BIT(n+1)
for i in range(n):
    bit.add(i, 1)

ret = 0
for i in range(n):
    c = bit.sum(a[i] - 1)
    bit.add(a[i], -1)
    ret += c*fac[n-i-1]
    ret %= mod
print((ret+1)%mod)