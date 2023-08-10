#####################################
mod = 998244353
n = int(input())
s = [int(x) for x in input()]
for i in range(n-1):
    if s[i]!=1 and s[i+1]!= 1: exit(print(-1))

ret = 0
for si in s[1:][::-1]:
    ret = ((ret+1) * si) % mod
print(ret%mod)
