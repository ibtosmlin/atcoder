# https://atcoder.jp/contests/abc299/tasks/abc299_g
n, m = map(int, input().split())
a = list(map(int, input().split()))

fix = [False] * (m+1)
change = [-1] * (m+1)
prev = 0
for i, ai in enumerate(a):
    if fix[ai]: continue
    if prev < ai: fix[prev] = True
    change[ai] = i
    prev = ai

ret = []
for i in range(1, m+1):
    ret.append((change[i], i))
ret.sort()
ret = [ri[1] for ri in ret]
print(*ret)