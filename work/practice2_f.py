# https://atcoder.jp/contests/practice2/tasks/practice2_f
import sys
from itertools import *
from operator import itemgetter
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
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)] + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])
# https://atcoder.jp/contests/atc001/tasks/fft_c

def convolve(a, b):
    def fft(f):
        d = n // 2
        v = w
        while d >= 1:
            u = 1
            for i in range(d):
                for j in range(i, n, 2*d):
                    f[j], f[j+d] = (f[j] + f[j+d]) % p, u * (f[j] - f[j+d]) % p
                u = u * v % p
            v = v * v % p
            d //= 2

    def ifft(f):
        d = 1
        while d < n:
            v = pow(invw, n // (2 * d), p)
            u = 1
            for i in range(d):
                for j in range(i, n, 2*d):
                    f[j+d] *= u
                    f[j], f[j+d] = (f[j] + f[j+d]) % p, (f[j] - f[j+d]) % p
                u = u * v % p
            d *= 2

    p, g = 998244353, 5
    n0, n1 = len(a), len(b)
    n = 1 << (max(n0, n1) - 1).bit_length() + 1
    a = a + [0] * (n-n0)
    b = b + [0] * (n-n1)
    w = pow(g, (p - 1) // n, p)
    invw = pow(w, p-2, p)
    fft(a), fft(b)
    for i in range(n):
        a[i] = a[i] * b[i] % p
    ifft(a)
    invn = pow(n, p - 2, p)
    return [a[i] * invn % p for i in range(n0 + n1 - 1)]

n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

print(*convolve(A, B))
