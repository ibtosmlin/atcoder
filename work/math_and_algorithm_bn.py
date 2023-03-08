n = int(input())
lr = [list(map(int, input().split())) for _ in range(n)]
lr.sort(key=lambda x:x[1])
ret = 0
now = 0
for l, r in lr:
    if now <= l:
        ret += 1
        now = r

print(ret)