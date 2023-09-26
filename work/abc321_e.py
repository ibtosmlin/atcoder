# https://atcoder.jp/contests/abc321/tasks/abc321_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

def calc(x, k, n):
    if k < 0: return 0
    # xからk個下がる
    l, r  = x, x
    for i in range(min(60,k)):
        l, r = 2*l, 2*r + 1
        if l > n: return 0
#    print(x, k, n, ">", max(0,min(r, n) - l + 1))
    return max(0,min(r, n) - l + 1)

def solve():
    n, x, k = map(int, input().split())
    ret = calc(x, k, n)
    p = x // 2
    while p >= 1:
        k -= 1
        if 2*p == x:
            u = x + 1
        else:
            u = x - 1

        if k == 0:
            ret += 1
        elif k >= 1:
            ret += calc(u, k-1, n)
        else:
            break
        x = p
        p //= 2

    print(ret)


t = int(input())
for _ in range(t):
    solve()