#name#
# ローリングハッシュ
#description#
#body#
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bd

class RollingHash():
    def __init__(self, s:str, base, mod):
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
        # returns hashvalue of [l, r]
        if l > r: return False
        r = min(self.length, r)
        return (self.h[r] - self.h[l-1] * self.pw[r-l+1]) % self.mod

base = 31; mod = 10**9+7
n, q = map(int, input().split())
S = input()
RHS = RollingHash(S, base, mod)

for _ in range(q):
    a, b, c, d = map(int, input().split())
    hash1 = RHS.get(a, b)
    hash2 = RHS.get(c, d)

    if hash1 == hash2:
        print('Yes')
    else:
        print('No')

#prefix#
# Lib_C_RollingHash
#end#