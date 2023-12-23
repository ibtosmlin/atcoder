# https://atcoder.jp/contests/abc332/tasks/abc332_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from itertools import *
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

def _compress(points:list) -> list:
    sx = set(points)
    pos = {xi:i for i, xi in enumerate(sorted(set(sx)))}
    return [pos[xi] for xi in points]

def inv_numbers(a: list, compress=False) -> int:
    _a = _compress(a) if compress else a
    bit = BIT(max(_a) + 2)
    ret = 0
    for i, ai in enumerate(_a):
        ret += i - bit.sum(ai); bit.add(ai, 1)
    return ret

###################################

H, W = map(int, input().split())
PH = list(permutations(range(H)))
PW = list(permutations(range(W)))

A = [list(map(int, input().split())) for _ in range(H)]
B = [list(map(int, input().split())) for _ in range(H)]

def check(ph, pw):
    for h, _h in enumerate(ph):
        for w, _w in enumerate(pw):
            if B[h][w] != A[_h][_w]: return False
    return True

ret = 10**10
for ph in permutations(range(H)):
    for pw in permutations(range(W)):
        if check(ph, pw):
            ret = min(ret, inv_numbers(list(ph))+inv_numbers(list(pw)))

if ret == 10**10:
    print(-1)
else:
    print(ret)