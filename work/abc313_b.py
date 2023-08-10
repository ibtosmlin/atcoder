# https://atcoder.jp/contests/abc313/tasks/abc313_b
n, m = map(int, input().split())
ret = [True] * (n+1)
ret[0] = False
for _ in range(m):
    a, b = map(int, input().split())
    ret[b] = False
if sum(ret) == 1:
    for i in range(n):
        if ret[i]: exit(print(i+1))
print(-1)