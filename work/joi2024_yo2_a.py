# https://atcoder.jp/contests/joi2024yo2/tasks/joi2024_yo2_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n = int(input())
a = list(map(int, input().split()))
u = [False] * 200_005
for ai in a:
    u[ai] = True
for i in range(200001):
    if u[i] and u[i+3] and u[i+6]:
        exit(print('Yes'))
print('No')