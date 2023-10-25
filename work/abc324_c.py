# https://atcoder.jp/contests/abc324/tasks/abc324_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

import re

n, t = input().split()
n = int(n)
t = list(t)

class RollingHash:
    def __init__(self, s:str, base=31, mod=10**9+7):
        self.mod = mod
        self.pw = pw = [1]*(len(s)+1)
        self.length = l = len(s)
        self.h = h = [0]*(l+1)
        v, t = 0, 1
        for i in range(l):
            v, t = v * base, t * base
            v += ord(s[i])
            v, t = v % mod, t % mod
            h[i+1], pw[i+1] = v, t

    def get(self, l, r):
        # returns hashvalue of [l, r)
        return (self.h[r] - self.h[l] * self.pw[r-l]) % self.mod


RHT = RollingHash(t)

def isok(s):
    if s == t: return True
    if len(s) == len(t):
        cnt = 0
        for i in range(len(s)):
            if s[i] != t[i]: cnt += 1
        if cnt == 1: return True
    RHS = RollingHash(s)
    if len(s) == len(t) + 1:
        for i in range(len(s)):
            if RHS.get(0, i) == RHT.get(0, i) and RHS.get(i+1, len(s)) == RHT.get(i, len(t)):
                return True
    if len(t) == len(s) + 1:
        for i in range(len(t)):
            if RHT.get(0, i) == RHS.get(0, i) and RHT.get(i+1, len(t)) == RHS.get(i, len(s)):
                return True
    return False


ret=[]
for i in range(n):
    s = list(input())
    if isok(s):
        ret.append(i+1)

print(len(ret))
print(*ret)

# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bd
