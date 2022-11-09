def end(r=-1): print(r); exit()
INF = float('inf')
A, K = input().split()
K = int(K)

if K == 10: end(0)
# K文字を使う状態を探す
used = set()
l = -1
for i, ai in enumerate(A):
    if len(used) == K-1 and not ai in used:
        l = i
        break
    used.add(int(ai))

print(l, used)

dp = [[INF] * 3 for _ in range(len(A)+1)]
dp[l][0] = 0
for i in range(l, len(A)):
    ai = A[i]
    # 選べる>選ぶ-以下が確定


    # 選べる>選ぶ-より大きいが確定


    # 選べる>usedからやりくり>選べる
    for ai in used

    # 選べない>usedからやりくり>選べる
    for ai in used



    print(ai)