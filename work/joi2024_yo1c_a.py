# https://atcoder.jp/contests/joi2024yo1c/tasks/joi2024_yo1c_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
h = int(input())
m = int(input())
print(h*60+m)