import sys
from itertools import *
from operator import itemgetter
from bisect import *
from collections import defaultdict, Counter, deque
from heapq import heapify, heappop, heappush
from functools import lru_cache
sys.setrecursionlimit(10001000)
INF = float('inf')
mod = 1000000007; mod1 = 998244353
PI = 3.141592653589793
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def end(r=-1): print(r); exit()
class Loop():
    """ループを検索して計算量圧縮

        Parameters
        ----------
        n : int
            鳩の巣の数
        x : int
            初期値
        f : function
            次の値を決める関数

        Notes
        ----------
        0->1->...->s_t-1 -> st->...-> s_t+x─┐
                             └─────────┘
        https://atcoder.jp/contests/typical90/tasks/typical90_bf

    """
    def __init__(self, n, x, f, g):
        self.hole = n
        self.ini_p = x
        self.nextp = f
        self.value = g
        self.__build()


    def __build(self):
        x = self.ini_p
        seen = defaultdict(int)
        seqs = []
        for i in range(self.hole + 10):
            seen[x] = i
            seqs.append(x)
            x = self.nextp(x)
            if x in seen: break
        p = seen[x]
        self.ini_seq = self.sequence([self.value(pos) for pos in seqs[:p]])
        self.lp_seq = self.sequence([self.value(pos) for pos in seqs[p:]])


    def get_kth(self, k:int)->int:
        """k番目の値を取得
        0-index
        """
        if k < self.ini_seq.len:
            return self.ini_seq.seq[k]
        else:
            k -= self.ini_seq.len
            _, k = divmod(k, self.lp_seq.len)
            return self.lp_seq.seq[k]


    def sum_kth(self, k:int)->int:
        """k番目までの値の累積和を取得
        0-index
        """
        if k < self.ini_seq.len:
            return self.ini_seq.acc[k]
        else:
            k -= self.ini_seq.len
            t, k = divmod(k, self.lp_seq.len)
            ret = self.ini_seq.acclast
            ret += self.lp_seq.acclast * t
            ret += self.lp_seq.acc[k]
            return ret


    class sequence:
        def __init__(self, seq):
            self.seq = seq          # 配列
            self.len = len(seq)     # 配列の個数
            self.acc = list(accumulate(seq))    # 配列の累積和
            if self.len == 0:
                self.acclast = 0    # 配列の累積和
            else:
                self.acclast = self.acc[-1]    # 配列の累積和


n, q, x = map(int, input().split())
w = list(map(int, input().split()))
s = sum(w)
b, x = divmod(x, s)
if x == 0:
    x += s
    b -= 1

rw = [0]
for wi in w*2:
    rw.append(rw[-1] + wi)

next = [-1] * n
for i in range(n):
    next[i] = bisect_left(rw, x + rw[i]) % n

def f(u):
    return next[u]

def g(u):
    nu = f(u)
    if nu <= u:
        nu += n
    return nu - u + b * n

lp = Loop(n, 0, f, g)

for _ in range(q):
    k = int(input())
    k -= 1
    print(lp.get_kth(k))
