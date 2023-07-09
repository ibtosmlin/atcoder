# https://atcoder.jp/contests/arc163/tasks/arc163_b
n, m = map(int, input().split())
a = list(map(int, input().split()))
a1 = a[0]
a2 = a[1]
b = sorted(a[2:])


ret = 10 ** 10
for i in range(n-2):
    if i+m-1==n-2: break
    now = max(0, a1 - b[i]) + max(0, b[i+m-1] - a2)
    ret = min(ret, now)

print(ret)
