# https://atcoder.jp/contests/past202303-open/tasks/past202303_k
from functools import lru_cache
N, t, p = map(int, input().split())
A = list(map(int, input().split()))

@lru_cache(10**6)
def e(i=0, pen=False):
    if i == N: return 0
    if pen: return 0
    ai = A[i]
    # aiを配る
    #takahashi
    # (ai * t) // 100 を入れる
    e1 = (ai - (ai*t) // 100) + e(i+1, False)
    # なにも入れない
    e2 = (ai + e(i+1, False)) * (1 - p/100) +  (ai - (ai*t) // 100 + e(i+1, True) ) * (p/100)
    return max(e1, e2)

print(e())





