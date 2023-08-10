# https://atcoder.jp/contests/past202303-open/tasks/past202303_j
from collections import defaultdict
h, w = map(int, input().split())

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

S = []
for _ in range(h):
    hash = RollingHash(input()*2)
    S.append(hash)

T = []
for _ in range(h):
    hash = RollingHash(input())
    T.append(hash)

for i in range(w):
    isok = True
    for j in range(h):
        if S[j].get(i, i+w) != T[j].get(0, w):
            isok = False
            break
    if isok:
        print('Yes')
        exit()
print('No')



# hシフトをw回繰り返す
# wが小さければOK
# wが大きければ

