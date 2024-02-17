# https://atcoder.jp/contests/abc341/tasks/abc341_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
int1=lambda x: int(x) - 1

N, M = map(int, input().split())
edges = [list(map(int1, input().split())) for _ in range(M)]
W = list(map(int, input().split()))
A = list(map(int, input().split()))
B = [1] * N
G = [[] for _ in range(N)]
for a, b in edges:
    if W[a] < W[b]:
        G[b].append((W[a], a))
    elif W[a] > W[b]:
        G[a].append((W[b], b))

WORD = [(wi, i) for i, wi in enumerate(W)]
WORD.sort()
ret = 0
for wx, x in WORD:
    dp = [0] * wx
    for wy, y in G[x]:
        for v in range(wx)[::-1]:
            if v-wy < 0: break
            if dp[v] < dp[v-wy] + B[y]:
                dp[v] = dp[v-wy] + B[y]
    B[x] += max(dp)
    ret += A[x] * B[x]
print(ret)
