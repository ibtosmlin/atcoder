# https://atcoder.jp/contests/abc296/tasks/abc296_d
n, m = map(int, input().split())
n2 = n**2
if m > n2:
    print(-1)
    exit()

ret = n2
for u in range(1, min(n, 10**6+1)):
    v = (m + (u - 1))// u
    if v > n: continue
    ret = min(ret, v * u)
    if v == 1: break
print(ret)


