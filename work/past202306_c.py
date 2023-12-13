# https://atcoder.jp/contests/past15-open/tasks/past202306_c
X, Y, R, N = map(int, input().split())

ret = [[None] * (2*N+1) for _ in range(2*N+1)]
for i in range(-N, N+1):
    for j in range(-N, N+1):
        if (i-X)**2 + (j-Y)**2 <= R**2:
            u = "#"
        else:
            u = "."
        ret[i+N][j+N] = u
for x in ret:
    print(*x)