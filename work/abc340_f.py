# https://atcoder.jp/contests/abc340/tasks/abc340_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

def gcd(m, n):
    r = m % n
    return gcd(n, r) if r else n

def extgcd(a, b):
    x, y = 1, 0
    s, t = 0, 1
    while b:
        q, r = a // b, a % b
        x, s = s, x - s*q
        y, t = t, y - t*q
        a, b = b, r
    return x, y, a

X, Y = map(int, input().split())

x, y = abs(X), abs(Y)
ret = None
if x == 0:
    if y == 1:
        ret = [2, 0]
    elif y == 2:
        ret = [1, 0]
    else:
        exit(print(-1))

elif y == 0:
    if x == 1:
        ret = [0, 2]
    elif x == 2:
        ret = [0, 1]
    else:
        exit(print(-1))

else:
    g = gcd(y, x)
    if not (g == 1 or g == 2): exit(print(-1))
    u = extgcd(x, y)
    if g == 2:
        ret = [u[1], u[0]]
    else:
        ret = [u[1]*2, u[0]*2]

for i in [1, -1]:
    for j in [1, -1]:
        a = i * ret[0]
        b = j * ret[1]
        if abs(X * b - Y * a) == 2:
            exit(print(a, b))
