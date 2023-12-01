# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

def sec(h , m, s):
    t = s
    t += m * 60
    t += h * 60 * 60
    return t

def solve():
    h0, m0, s0, h1, m1, s1 = map(int, input().split())
    h = sec(h1, m1, s1) - sec(h0, m0, s0)
    h, s = divmod(h, 60)
    h, m = divmod(h, 60)
    print(h, m, s)

for _ in range(3):
    solve()
