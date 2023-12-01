# https://atcoder.jp/contests/abc329/tasks/abc329_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n = int(input())
print(sorted(list(set(map(int, input().split()))))[-2])
