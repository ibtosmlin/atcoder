# https://atcoder.jp/contests/typical90/tasks/typical90_au
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
s = input()
t = input()

x = [[None] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if s[i] == t[j]:
            