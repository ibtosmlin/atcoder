# https://atcoder.jp/contests/abc295/tasks/abc295_b
r, c = map(int, input().split())
b = [list(input()) for _ in range(r)]
ret = [['.']*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if b[i][j] == '#':
            ret[i][j] = '#'

for i in range(r):
    for j in range(c):
        if not b[i][j] in '123456789': continue
        bm = int(b[i][j])
        for u in range(-10, 10):
            for v in range(-10, 10):
                if 0<=i+u<r and 0<=j+v<c and abs(u)+abs(v) <= bm:
                    ret[i+u][j+v] = '.'

for ri in ret:
    print(''.join(ri))