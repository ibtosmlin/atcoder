n, s = map(int, input().split())
ret = 0
for r in range(1, n+1):
    b = min(n, max(s - r, 0))
    ret += b
print(ret)
