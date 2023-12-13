# https://atcoder.jp/contests/past15-open/tasks/past202306_k
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
# 転倒数
# 配列中 i<j, ai>ajとなるものの個数
# https://atcoder.jp/contests/chokudai_S001/tasks/chokudai_S001_j
class BIT:
    def __init__(self, size):
        self.size = size; self.dat = [0]*(size+1)

    def add(self, i, x):
        i += 1
        while i <= self.size: self.dat[i] += x; i += i & -i

    def sum(self, r):
        r += 1; s = 0
        while r: s += self.dat[r];r -= r & -r
        return s


def inv_numbers(a: list, compress=False) -> int:
    bit = BIT(max(_a) + 2)
    ret = 0
    for i, ai in enumerate(_a):
        ret += i - bit.sum(ai); bit.add(ai, 1)
    return ret

###################################

n = int(input())
P = [0] + list(map(int, input().split()))
n += 1
t = 0
C = BIT(n+1)
V = BIT(n+1)

ret = 0
for i, pi in enumerate(P):
    ret += (i - C.sum(pi)) * pi
    ret += t - V.sum(pi)
    t += pi
    C.add(pi, 1)
    V.add(pi, pi)
print(ret)
