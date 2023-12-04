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

#name#
# 動的ローリングハッシュ(１点更新)
#description#
#body#
# https://atcoder.jp/contests/abc331/tasks/abc331_f

class DynamicRollingHash:
    def __init__(self, s:str, base=31, mod=10**9+7):
        self.mod = mod
        self.size = l = len(s)
        self.h = h = [0]*(l+1)
        self.pw = [1] * (l+1)
        self.ipw = [1] * (l+1)
        invbase = pow(base, mod-2, mod)
        for i in range(l):
            self.pw[i+1] = self.pw[i] * base % mod
            self.ipw[i+1] = self.ipw[i] * invbase % mod
            self.update(i, s[i])

    def update(self, i, c):
        cv = (ord(c) * self.pw[i] % self.mod - self[i]) % self.mod
        self._add(i, cv)


    def _add(self, i, x):
        i += 1
        while i <= self.size:
            self.h[i] += x
            i += i & -i

    def get(self, l, r):
        return self._range_sum(l, r) * self.ipw[l] % self.mod


    def _sum(self, r):  #returns sum of [0, r)
        ret = 0
        while r>0:
            ret = (ret + self.h[r]) % self.mod
            r -= r & -r
        return ret


    def _range_sum(self, l, r):  #returns sum of [l, r)
        if l == 0:
            return self._sum(r)
        else:
            return (self._sum(r) - self._sum(l)) % self.mod


    def __getitem__(self, i):
        return (self._sum(i+1) - self._sum(i))%self.mod


n, q = map(int, input().split())
s = input()
left = DynamicRollingHash(s)
right = DynamicRollingHash(s[::-1])

for _ in range(q):
    query = list(input().split())
    if query[0] == "1":
        x, c = query[1:]
        x = int(x) - 1
        left.update(x, c)
        right.update(n-1-x, c)
    else:
        l, r = map(int, query[1:])
        print('Yes' if left.get(l-1, r) == right.get(n-r, n-l+1) else 'No')

#prefix#
# Lib_Str_RollingHash
#end#