# https://atcoder.jp/contests/arc145/tasks/arc145_c

n = int(input())
# 2^n * (2*n)! / (n+1)!
# 2^n * 2*n ～ n+2
mod = 998244353
ret = pow(2, n, mod)
for i in range(n+2, 2*n+1):
    ret *= i
    ret %= mod
print(ret)