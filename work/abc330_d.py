# https://atcoder.jp/contests/abc330/tasks/abc330_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
S = [input() for _ in range(n)]

ret = 0
R = [0] * n
C = [0] * n
for i in range(n):
    for j in range(n):
        if S[i][j] == "o":
            R[i] += 1
            C[j] += 1

for i in range(n):
    for j in range(n):
        if S[i][j] == "o":
            ret += (R[i] - 1) * (C[j] - 1)
print(ret)
