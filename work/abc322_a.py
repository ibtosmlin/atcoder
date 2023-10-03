# https://atcoder.jp/contests/abc322/tasks/abc322_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
s = input()
for i in range(n-2):
    if s[i:i+3] == 'ABC':
        exit(print(i+1))
print(-1)