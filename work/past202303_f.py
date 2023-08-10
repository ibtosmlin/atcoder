# https://atcoder.jp/contests/past202303-open/tasks/past202303_f

n = int(input())
S = set(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    m = int(input())
    cnt = n
    T = set(map(int, input().split()))
    for ti in T:
        if ti in S: continue
        cnt += 1
    print(cnt)