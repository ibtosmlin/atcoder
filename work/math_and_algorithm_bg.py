# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bg
mod = 1000000007; mod1 = 998244353
n = int(input())
a = list(map(int, input().split()))
a.sort()
ret, p2 = 0, 1
for i in range(n):
    ret += a[i] * p2
    ret %= mod
    p2 *= 2
    p2 %= mod

print(ret)
