# https://atcoder.jp/contests/abc328/tasks/abc328_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

s = list(input())
n = len(s)
dp = []

for i in range(n):
    dp.append(s[i])
    if len(dp) >= 3 and dp[-3] == 'A' and dp[-2] == 'B' and dp[-1] == 'C':
        dp.pop()
        dp.pop()
        dp.pop()
print("".join(dp))
