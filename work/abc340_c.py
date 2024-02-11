import sys; sys.setrecursionlimit(10001000)
from functools import lru_cache
@lru_cache(1000000)
def f(x):
    if x == 1: return 0
    return x + f(x//2) + f(x-x//2)
print(f(int(input())))