# https://atcoder.jp/contests/past16-open/tasks/past202309_h
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
N, M = map(int, input().split())
A = list(map(int, input().split()))

dpn = [[-1 for _ in range(M+1)] for _ in range(N+1)]
dpd = [[-1 for _ in range(M+1)] for _ in range(N+1)]
dpn[0][0] = 0

for i in range(N):
    for j in range(M):
        if dpn[i][j] != -1:
            dpn[i+1][j] = max(dpn[i+1][j], dpn[i][j] + A[i])
            dpd[i+1][j+1] = max(dpd[i+1][j+1], dpn[i][j])
        if dpd[i][j] != -1:
            dpn[i+1][j] = max(dpn[i+1][j], dpd[i][j] + A[i])
    if dpd[i][M] != -1:
        dpn[i+1][M] = max(dpn[i+1][M], dpd[i][M] + A[i])
    if dpn[i][M] != -1:
        dpn[i+1][M] = max(dpn[i+1][M], dpn[i][M] + A[i])

print(max(dpn[-1][M], dpd[-1][M]))