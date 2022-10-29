# https://atcoder.jp/contests/abc275/tasks/abc275_d
memo= dict()
memo[0] = 1
def f(k):
    if k in memo: return memo[k]
    memo[k] = ret = f(k//2) + f(k//3)
    return ret
print(f(int(input())))
