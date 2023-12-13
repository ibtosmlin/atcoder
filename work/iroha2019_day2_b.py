# https://atcoder.jp/contests/iroha2019-day2/tasks/iroha2019_day2_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

x, y = map(int, input().split())
a, b = map(int, input().split())
sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

def line(u, v):
    return (v-a)*x-(b-a)*u

if line(sx, sy) * line(tx, ty) > 0:
    print('No')
else:
    print('Yes')