n, k = map(int, input().split())
s = input()

cnts = [[0] * (n+1) for _ in range(26)]
for i, si in enumerate(s):
    u = ord(si) - ord('a')
    cnts[u][i+1] += 1
for i in range(26):
    for j in range(n):
        cnts[i][j+1] += cnts[i][j]

def f(l):
    return tuple(cnt[l+k]-cnt[l] for cnt in cnts)

d = dict()

for l in range(n-k+1):
    u = f(l)
    if u in d:
        if d[u] <= l:
            print('YES')
            exit()
    else:
        d[u] = l + k

print('NO')
