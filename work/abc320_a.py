# https://atcoder.jp/contests/abc320/tasks/abc320_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

a, b = map(int, input().split())
print(pow(a, b) + pow(b, a))