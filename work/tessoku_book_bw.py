n = int(input())
ps = [list(map(int, input().split())) for _ in range(n)]
ps.sort(key=lambda x:x[1])
now = 0
ret = 0
for t, d in ps:
    if now + t <= d:
        ret += 1
        now += t
print(ret)