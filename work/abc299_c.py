# https://atcoder.jp/contests/abc299/tasks/abc299_c
n = int(input())
s = input()
nw = 0
mx = 0
for si in s:
    if si == 'o':
        nw += 1
    else:
        mx = max(mx, nw)
        nw = 0
mx = max(mx, nw)
if mx == 0 or mx == n:
    print(-1)
else:
    print(mx)