# https://atcoder.jp/contests/past202209-open/tasks/past202209_e
R, N, M, L = map(int, input().split())
S = list(map(int, input().split()))

round = 0
remove = 0
throw = 0

for i in range(L):
    remove += S[i]
    throw += 1
    if throw == M or remove == N:
        round += 1
        remove = 0
        throw = 0
        continue
    if i == L-1:
        print('No'); exit()
    if remove + S[i+1] > N:
        print('No'); exit()

if round == R:
    print('Yes')
else:
    print('No')


