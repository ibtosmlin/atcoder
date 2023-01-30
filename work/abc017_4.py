mod = 10 ** 9 + 7
n, m = map(int, input().split())
s = [int(input()) for _ in range(n)]


dp = [0] * (n+1)
dp[0] = 1
rdp = [0] * (n+2)
rdp[1] = 1
used = set()

l = 0
for r in range(n):
    while s[r] in used:
        used.remove(s[l])
        l += 1
#    print(l, used)
    used.add(s[r])
#    print(used)
    dp[r+1] = rdp[r+1] - rdp[l]
    dp[r+1] %= mod
    rdp[r+2] = rdp[r+1] + dp[r+1]
    rdp[r+2] %= mod
print(dp[-1]%mod)
