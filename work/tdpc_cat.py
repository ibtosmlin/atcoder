# https://atcoder.jp/contests/tdpc/tasks/tdpc_cat
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
F = [list(map(int, input().split())) for _ in range(n)]

# 選べるのは２つまで

dp = [[] for _ in range(n)]