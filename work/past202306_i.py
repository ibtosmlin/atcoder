n, k = map(int, input().split())
a = list(map(int, input().split()))
N = 1000002
C = [0] * N
for ai in a:
    C[ai] += 1

ret = 1
for j in range(1, N):
    u = 0
    for ij in range(j, N, j):
        u += C[ij]
    if u >= k:
        ret = j
print(ret)