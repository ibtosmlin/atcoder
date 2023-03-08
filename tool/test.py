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

class permutation:
    def __init__(self, L):
        self.n = len(L)
        self.L = L
        self.LS = sorted(L[:])
        self.map = {li: i for i, li in enumerate(self.LS)}
        nn = self.n + 1
        fa = [1] * (nn + 1)
        for i in range(nn):
            fa[i+1] = fa[i] * (i+1)
        self.fa = fa
        self.convL = self._convL(self.L)
        self.facn = self.fa[self.n]
        self.k = self.id_of_permutation(self.L)

    def _convL(self, L):
        return [self.map[li] for li in L]

    def _restoreP(self, P):
        return [self.LS[i] for i in P]

    def _kth_permutation(self, k):
        # zero-indexed here
        n = self.n
        S = [i for i in range(n)]
        L = []
        for i in range(n):
            a = self.fa[n-1-i]
            j = k // a
            k %= a
            L.append(S[j])
            S = S[:j] + S[j+1:]
        return L

    def _id_of_permutation(self, P):
        # zero-indexed here
        ret = 0
        while len(P) > 1:
            a = len([l for l in P if l < P[0]])
            ret += a * self.fa[len(P) - 1]
            P = P[1:]
        return ret

    def id_of_permutation(self, L=None)->int:
        """
        return: 順列の辞書順
        """
        if L:
            P = self._convL(L)
            return self._id_of_permutation(P)
        else: return self.k

    def kth_permutation(self, k)->list:
        """
        return: k番目の順列
        """
        P = self._kth_permutation(k)
        return self._restoreP(P)

    def prev(self, L=None):
        """
        return: 初期順列または入力順列のひとつ前
        """
        if L:
            k = self.id_of_permutation(L)
        else:
            k = self.k
        if k == 0: return None
        return self.kth_permutation(self.k - 1)

    def next(self, L=None):
        if L:
            k = self.id_of_permutation(L)
        else:
            k = self.k
        if k + 1 == self.facn: return None
        return self.kth_permutation(k + 1)

##################################
N = int(input())
P = [int(a) for a in input().split()]
mut = permutation(P)
print(*mut.prev())
P = list(permutations(range(n), r))   # 順列(nPr)
C = list(combinations(range(n), r))   # 組み合わせ(nCr)
CR = list(combinations_with_replacement(range(n), r))  # 重複も許容した組み合わせ(nHr=n+r-1Cr)
PN = list(product(range(n), repeat=r)) # 重複順列(n**r)
T = [[1, 2],[3, 4, 5, 6],[7, 8, 9]]
PT = list(product(*T))