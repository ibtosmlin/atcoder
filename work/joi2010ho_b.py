n = int(input())
A = [int(input()) for _ in range(n-1)]
A.append(0)
# dpA[i] 右端がAでA-B = i である時の最低コスト
INF = 10 ** 9
of = n+1
dpA = [INF] * (2*of)
dpB = [INF] * (2*of)
dpA[of] = 0

for i, ai in enumerate(A):
    ndpA = [INF] * (2*of)
    ndpB = [INF] * (2*of)
    for j in range(of-i, of+i+1, 2):
        ndpA[j+1] = min(ndpA[j+1], dpA[j], dpB[j]+ai)
        ndpB[j-1] = min(ndpB[j-1], dpA[j]+ai, dpB[j])
    dpA, dpB = ndpA, ndpB
print(dpA[of])
