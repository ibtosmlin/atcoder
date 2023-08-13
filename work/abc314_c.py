# https://atcoder.jp/contests/abc314/tasks/abc314_c
n, m = map(int, input().split())
s = input()
c = list(map(int, input().split()))

st = [[] for _ in range(m+1)]
cnt = [0 for _ in range(m+1)]
for si, ci in zip(s, c):
    st[ci].append(si)
    cnt[ci] += 1

now = [-1 for _ in range(m+1)]

ret = []
for ci in c:
    ret.append(st[ci][now[ci]])
    now[ci] += 1
print("".join(ret))

