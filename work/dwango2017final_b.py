# https://atcoder.jp/contests/dwacon2017-honsen/tasks/dwango2017final_b
from itertools import *
from operator import itemgetter
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
import sys
sys.setrecursionlimit(10001000)
INF = float('inf'); INF1 = 10 ** 9
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
yes = 'Yes'; no = 'No'
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def end(r=-1): print(r); exit()

##############################
# 素数出力 O(n**0.5)
# n <= 10**5
##############################
def get_primes(n:int) -> list:
# n以下の素数列挙
    n += 1
    IsPrime = [True] * n
    IsPrime[0], IsPrime[1] = False, False
    for p in range(n):
        if not IsPrime[p]: continue
        for j in range(p*2, n, p):
            IsPrime[j] = False
    ret = [p for p in range(n) if IsPrime[p]]
    return ret

primes = get_primes(10**5)

class _Mo:
    def __init__(self, N:int):
        self.N=N
        self.query = []
        self.Q = 0
        self.shift = 20
    def add_query(self, l:int, r:int): # [l,r)
        self.query.append((l,r))
        self.Q += 1
    def solve(self):
        assert max(self.N, self.Q)<(1<<self.shift)
        block_size = self.N // (min(self.N, int(len(self.query)**0.5+0.5)))
        query = [None] * self.Q
        for i,(l,r) in enumerate(self.query):
            L = l // block_size
            query[i] = (L<<(2*self.shift))+((r if L&1 else -r)<<self.shift) + i
        query.sort()
        L=R=0
        ret = [0]*self.Q
        mask=(1<<self.shift)-1
        for q in query:
            i = q&mask
            l,r=self.query[i]
            while l<L:
                L-=1;
                self.add_left(L)
            while L<l:
                self.remove_left(L)
                L+=1
            while R<r:
                self.add_right(R)
                R+=1
            while r<R:
                R-=1
                self.remove_right(R)
            ret[i] = self.get_state()
        return ret


mod = 10**9+7
N,Q=map(int,input().split())
X=[int(input()) for _ in range(N)]
XS = set(X)
PS = dict()
for xi in XS:
    x = xi
    f = []
    for q in primes:
        if q > x: break
        if x % q == 0:
            cnt = 0
            while x % q == 0:
                cnt += 1
                x //= q
            f.append([q, cnt])
    PS[xi] = f

memo = dict()
def modinvs(u):
    if u in memo:
        return memo[u]
    memo[u] = modinv(u, mod)
    return memo[u]


class Mo(_Mo):
    def __init__(self, N):
        super().__init__(N)
        self.count = defaultdict(int)
        self.value = 1
    def get_state(self):
        return self.value%mod
    def add_left(self, i):
        for k, v in PS[X[i]]:
            self.value *= modinvs(1+self.count[k])
            self.count[k] += v
            self.value *= 1+self.count[k]
            self.value %= mod

    def remove_left(self, i):
        for k, v in PS[X[i]]:
            self.value *= modinvs(1+self.count[k])
            self.count[k] -= v
            self.value *= 1+self.count[k]
            self.value %= mod

    add_right = add_left
    remove_right = remove_left


mo = Mo(N)
for _ in range(Q):
    l,r=map(int,input().split())
    mo.add_query(l-1,r)
ans = mo.solve()

print("\n".join(map(str,ans)))


