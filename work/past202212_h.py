d = int(input())
n = input()

ret = 0
cnt = [0] * 10
for i, ni in enumerate(n):
    ni = int(ni)
    for nj in range(10):
        ret += cnt[nj] * abs(nj - ni)
    cnt[ni] += 1

print(ret)
