# https://atcoder.jp/contests/utpc2013/tasks/utpc2013_02
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

shift = 2013
y, m = map(int, input().split())

months = y * 12 + m - shift * 12

def calmonth(years):
    return (13 + (13 + years - 1)) * years // 2

r = 10**18
l = 0
while r-l > 1:
    mid = (r+l)//2
    if calmonth(mid) < months:
        l = mid
    else:
        r = mid


print(l+shift, months-calmonth(l))
