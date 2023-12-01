# https://atcoder.jp/contests/joi2024yo1c/tasks/joi2024_yo1c_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
S = input()
for i in range(n-1):
    if S[i] != S[i+1]:
        exit(print('No'))
print('Yes')
exit()