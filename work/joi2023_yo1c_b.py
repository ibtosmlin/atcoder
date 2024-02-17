# https://atcoder.jp/contests/joi2023yo1c/tasks/joi2023_yo1c_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

a = int(input())
b = int(input())
print(int(a+b*7 <= 30))
