# https://atcoder.jp/contests/past15-open/tasks/past202306_f
n = int(input())
a = list(map(int, input().split()))
b = []
for i, ai in enumerate(a):
    b.append((ai, i))
b.sort()
for i in range(n):
    _, j = b[i]
    a[j] = i+1
print(*a)
