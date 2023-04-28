# https://atcoder.jp/contests/agc061/tasks/agc061_a
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
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'
def alp(i): return chr(ord('a') + i%26)    # i=0->'a', i=25->'z'
def modinv(x, mod): return pow(x, mod - 2, mod)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1
def notisinhw(i, j, h, w): return not ((0 <= i < h) and (0 <= j < w))
def yes(): print('Yes')
def no(): print('No')
def end(r=-1): print(r); exit()
def fstr(x): return f'{x:.10f}'

# N = 20

# def shuffle(l, r, A):
#     if r == l+1:
#         A[l], A[r] = A[r], A[l]
#         return A
#     A = shuffle(l, r-1, A)
#     A = shuffle(l+1, r, A)
#     return A

# for i in range(1, N-1):
#     A = [i for i in range(N)]
#     print(*shuffle(0, i, A))


def shuffle(l, r, k):
    def f(f, l, r, k):
        if k < l or r < k:
            return k
        if l + 1 ==r:
            if l == k: return r
            else: return l

    w = r - l - 1
    b = w & -w
    if b == 1:
        k = f(f, l+b, r, k)
        k = f(f, l, r-b, k)


t = int(input())

for _ in range(t):
    shuffle(l, r, k)


void solve() {
    ll n, k;
    cin>>n>>k;



      ll w = r-l-1;
      ll b = w&-w;
      if (b == 1) {
        k = f(f,l+b,r,k);
        k = f(f,l,r-b,k);
      } else {
        ll nk = (k-l)>>1, nw = w>>1;
        if ((nk&nw) == nk) {
          k -= l; k ^= 1; k += l;
        }
      }
      return k;
    };
    cout<<f(f,0,n-1,k-1)+1<<endl;