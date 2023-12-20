# https://atcoder.jp/contests/past16-open/tasks/past202309_l
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from sortedcontainers import SortedSet
from math import gcd

N, Q = map(int, input().split())
A = list(map(int, input().split()))
RA = [0]
for ai in A:
    RA.append(RA[-1]+ai)

class Obj:
    def __init__(self, l, r):
        self.l = l
        self.r = r
        self.bunshi = RA[r] - RA[l]
        self.bunbo = r - l

    def __lt__(self, other):
        return self.bunshi*other.bunbo - other.bunshi*self.bunbo < 0
    def __le__(self, other):
        return self.bunshi*other.bunbo - other.bunshi*self.bunbo <= 0
    def __eq__(self, other):
        return self.bunshi*other.bunbo - other.bunshi*self.bunbo == 0
    def __gt__(self, other):
        return self.bunshi*other.bunbo - other.bunshi*self.bunbo > 0
    def __ge__(self, other):
        return self.bunshi*other.bunbo - other.bunshi*self.bunbo >= 0

    def __str__(self):
        return f"{self.bunshi} {self.bunbo}"

V = SortedSet()

for _ in range(Q):
    que = list(map(int, input().split()))
    if len(que) == 2:
        x = que[1]
    else:
        print(V[0])
