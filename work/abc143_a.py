# https://atcoder.jp/contests/abc143/tasks/abc143_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
a, b = map(int, input().split())
print(max(0, a-b*2))