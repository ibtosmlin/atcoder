# https://atcoder.jp/contests/abc136/tasks/abc136_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

a, b, c = map(int, input().split())

x = a - b
x = min(x, c)
print(c-x) 