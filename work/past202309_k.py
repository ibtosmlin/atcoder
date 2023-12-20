# https://atcoder.jp/contests/past16-open/tasks/past202309_k
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

from collections import deque
n = int(input())
S = [input() for _ in range(n)]
direc = [(0, -1), (-1, 0), (0, 1), (1, 0)]
isinhw = lambda i,j,h,w: (0 <= i < h) and (0 <= j < w)
INF = 10**10
isok = [[0] * (n*n) for __ in range(4)]
start = -1
for i in range(n):
    for j in range(n):
        if S[i][j] == 'X': continue
        if S[i][j] == 'S': start = (i, j)
        for k in range(4): isok[k][i*n+j] = 1

for i in range(n):
    for j in range(n-1):
        isok[0][i*n+j+1] += isok[0][i*n+j] * isok[0][i*n+j+1]
    for j in range(1, n)[::-1]:
        isok[2][i*n+j-1] += isok[2][i*n+j] * isok[2][i*n+j-1]

for i in range(n):
    for j in range(n-1):
        isok[1][(j+1)*n+i] += isok[1][j*n+i] * isok[1][(j+1)*n+i]
    for j in range(1, n)[::-1]:
        isok[3][(j-1)*n+i] += isok[3][j*n+i] * isok[3][(j-1)*n+i]

def bfs(k):
    seen = [INF] * (n*n)
    que = deque()
    seen[start[0]*n+start[1]] = 0
    que.append(start)
    while que:
        i, j = que.popleft()
        for id, (di, dj) in enumerate(direc):
            if isok[id][i*n+j] - 1 < k: continue
            ni = i + di * k
            nj = j + dj * k
            if not isinhw(ni, nj, n, n): continue
            if seen[ni*n+nj] != INF: continue
            seen[ni*n+nj] = seen[i*n+j] + 1
            que.append((ni, nj))
            if S[ni][nj] == 'G': return seen[ni*n+nj]
    return -1

for k in range(1, n):
    print(bfs(k))
