# https://atcoder.jp/contests/arc140/tasks/arc140_c
n, x = map(int, input().split())
A = list(range(n))
x -= 1
ret = [None] * n
t = 0
if n%2 and x == n//2:
    pass
elif n%2==0 and x == n//2-1:
    A = A[::-1]
elif n%2==0 and x == n//2:
    pass
else:
    A.remove(x)
    n -= 1
    ret[t] = x+1
    t += 1

now = n // 2
direc = -1
for i in range(n):
    ret[t] = A[now]+1
    t += 1
    now += direc * (i+1)
    direc *= -1
print(*ret)
