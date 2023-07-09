# https://atcoder.jp/contests/arc029/tasks/arc029_2

def isok(a, b, c, d):
    if c >= a and d >= b: return True
    if c < a: False
    


a, b = map(int, input().split())
if a > b: a, b = b, a
n = int(input())
for _ in range(n):
    c, d = map(int, input().split())
    if c > d: c, d = d, c

    if c >= a and d >= b:
        print('YES')
    else:
        if a ** 2 + b ** 2 - d ** 2 < 0:
            print('NO')
            continue
        x = (a * d + (b ** 2 * (a ** 2 + b ** 2 - d ** 2)) ** 0.5) / (a ** 2 + b ** 2)
        y = (d - a * x) / b

        if b * x + a * y <= c:
            print('YES')
        else:
            print('NO')
