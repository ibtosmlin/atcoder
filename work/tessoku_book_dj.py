# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dj
from functools import lru_cache

@lru_cache(maxsize=100000)
def g(n):
    if n == 0: return 0
    #
    d = 1
    while n // (d*10):
        d *= 10
    x, y = divmod(n, d)
    # print(x, y, d)    # x=2, y=88, d=100
    ret = 0
    ret += g(n-y-1)     # 0 - 199の合計
    ret += x * (y + 1)  # 200 - 2** のx(2)の合計
    ret += g(y)         # 200 - 2** の00-**の合計
    return ret

n = int(input())
print(g(n))