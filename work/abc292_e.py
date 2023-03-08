from collections import deque
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x)-1, input().split())
    G[a].append(b)

ret = n * (n-1)
for i in range(n):
    seen = [0] * n
    que = deque()
    seen[i] = 1
    que.append(i)
    while que:
        x = que.popleft()
        for nx in G[x]:
            if seen[nx] == 1: continue
            seen[nx] = 1
            que.append(nx)
    ret -= n - sum(seen)
print(ret - m)


