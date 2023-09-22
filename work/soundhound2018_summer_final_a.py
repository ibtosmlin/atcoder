# https://atcoder.jp/contests/soundhound2018-summer-final/tasks/soundhound2018_summer_final_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

c, d = map(int, input().split())
l = 140
r = 170

def f(x):
    _l = l
    _r = r
    ret = 0
    while x > _r:
        ret += (_r - _l)
        _l *= 2
        _r *= 2
    return ret + max(x - _l, 0)

print(f(d)-f(c))


