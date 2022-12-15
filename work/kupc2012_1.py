# https://atcoder.jp/contests/kupc2012/tasks/kupc2012_1
n, t, e = map(int, input().split())
A = list(map(int, input().split()))
for i in range(n):
    for j in range(t-e, t+e+1):
        if j % A[i] == 0:
            print(i+1)
            exit()
print(-1)
