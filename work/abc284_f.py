n = int(input())
m = 2*n
t = input()
counts = [[0] * 26 for _ in range(m+1)]

for i, ti in enumerate(t):
    j = ord(ti) - ord('a')
    counts[i+1][j] += 1

for i in range(m):
    for j in range(26):
        counts[i+1][j] += counts[i][j]

rc = [0] * 26
for j in range(26):
    if counts[-1][j]%2:
        print(-1)
        exit()
    else:
        rc[j] = counts[-1][j] // 2

#print(rc)

for l in range(m-n):
    r = l + n
    rcn = [0] * 26
    for j in range(26):
        rcn[j] = counts[r][j] - counts[l][j]
    if rcn != rc:
        continue
    nt = t[l:r][::-1]
    if t[:l] + t[r:] == nt:
        print(nt)
        print(l)
        exit()
print(-1)