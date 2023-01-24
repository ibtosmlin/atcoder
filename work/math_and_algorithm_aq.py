# https://atcoder.jp/contests/tessoku-book/tasks/math_and_algorithm_aq
m = 10**9+7
a, b = map(int, input().split())
ret = 1
while b:
    if b%2:
        ret = ret * a % m
    b //= 2
    a = a * a % m
print(ret)