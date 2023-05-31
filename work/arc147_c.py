# https://atcoder.jp/contests/arc147/tasks/arc147_c
n = int(input())
ls = []
rs = []
for i in range(n):
    l, r = map(int, input().split())
    ls.append((l, i))
    rs.append((r, i))

ls.sort(reverse=True)
rs.sort()

lp = 0
rp = 0
point = []
while lp < n and rp < n and rs[rp][0] < ls[lp][0]:
    point.append(rs[rp][0])
    point.append(ls[lp][0])
    lp += 1
    rp += 1

if len(point) < n:
    point += [rs[rp][0]] * (n-len(point))

point.sort()

ret = 0
rsum = 0
for i, xi in enumerate(point):
    ret += i * xi - rsum
    rsum += xi
print(ret)
