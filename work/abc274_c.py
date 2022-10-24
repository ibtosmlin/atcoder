# https://atcoder.jp/contests/abc274/tasks/abc274_c
n = int(input())
a = list(map(int, input().split()))
g = [0, 0]
for i, ai in enumerate(a):
    ng = g[ai] + 1
    g.append(ng)
    g.append(ng)

for k in range(2*n+1):
    print(g[k+1])