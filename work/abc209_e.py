# https://atcoder.jp/contests/abc209/tasks/abc209_e
from collections import defaultdict, Counter, deque
win = 'Takahashi'
lose = 'Aoki'
draw = 'Draw'
n = int(input())
s = []
nodes = set()
for _ in range(n):
    si = input()
    fm = si[:3]
    to = si[-3:]
    nodes |= {fm, to}
    s.append((fm, to))

nodes = {node: i for i, node in enumerate(list(nodes))}
N = len(nodes)
G = [[] for _ in range(N)]
rG = [[] for _ in range(N)]
childs = [0 for _ in range(N)]
dp = [None] * N

que = deque([])

for fm, to in s:
    if fm == to:
        dp[fm] = draw
        que.append(fm)
    else:
        childs[fm] += 1
        rG[to].append(fm)
        G[fm].append(to)

for v in range(N):
    if childs[v] == 0 and dp[v] == None:
        dp[v] = win
        que.append(v)

while que:
    v = que.popleft()
    for x in rG[v]:
        childs[x] -= 1
        if childs[x] == 0 and dp[x] == None:
            for nv in G[x]:
                if dp[nv] == win:
                    dp[x] = lose
                    break
                if dp[nv] == lose:
                    
            que.append(x)






