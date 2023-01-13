class RollingHash():
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

n = int(input())
m = 2*n
T = input()

RHF = RollingHash(T[:n])
RHS = RollingHash(T[n:][::-1])

for l in range(n+1):
    hashF = (RHF.get(0, l), RHF.get(l, n))
    hashS = (RHS.get(n-l, n), RHS.get(0, n-l))
    if hashF == hashS:
        print(T[:l]+T[l:n][::-1])
        print(l)
        exit()
print(-1)
