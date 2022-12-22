# https://atcoder.jp/contests/joi2022yo1c/tasks/joi2022_yo1c_d
n, m = map(int, input().split())
BoxinBall = [i for i in range(n+1)]
for _ in range(m):
    x, y = map(int, input().split())
    BoxinBall[x] = y

print(*BoxinBall[1:])