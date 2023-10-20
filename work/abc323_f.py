# https://atcoder.jp/contests/abc323/tasks/abc323_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

x0, y0, x1, y1, x2, y2 = map(int, input().split())

x0, y0 = x0-x2, y0-y2
x1, y1 = x1-x2, y1-y2
if x1 < 0: x0, x1 = -x0, -x1
if y1 < 0: y0, y1 = -y0, -y1

def solve(x0, y0, x1, y1):
    if x1==0 and y1==0: return 0
    # x1 y1+1に移動する
    if y0<y1 and x0==x1:
        dist = y1+1-y0+2
    else:
        dist = abs(x0-x1) + abs(y1+1-y0)
    dist += y1
    if x1 != 0:
        dist += 2
        dist += x1
    return dist

ret = min(solve(x0, y0, x1, y1), solve(y0, x0, y1, x1))
print(ret)