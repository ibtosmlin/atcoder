#title#
# ローリングハッシュ
#subtitle#
# RollingHash: 文字列が一致しているか判定する

#name#
# ローリングハッシュ
#description#
#body#
# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_bd

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



q = int(input())
s = input()
RHS = RollingHash(s)

for _ in range(q):
    a, b, c, d = map(int, input().split())
    hash1 = RHS.get(a, b)
    hash2 = RHS.get(c, d)

    if hash1 == hash2:
        print('Yes')
    else:
        print('No')

#prefix#
# Lib_Str_RollingHash
#end#
