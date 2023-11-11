# https://atcoder.jp/contests/joi2023yo2/tasks/joi2023_yo2_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
a = list(map(int, input().split()))

ML = [-1] * n
mL = [10**10] * n
MR = [-1] * n
mR = [10**10] * n

# Left
for i in range(1, n):
    ML[i] = max(ML[i-1], a[i-1])
    mL[i] = min(mL[i-1], a[i-1])
# Right
for i in range(n-2, -1, -1):
    MR[i] = max(MR[i+1], a[i+1])
    mR[i] = min(mR[i+1], a[i+1])

M = [None] * n
m = [None] * n

for i in range(n):
    M[i] = max(ML[i], MR[i])
    m[i] = min(mL[i], mR[i])

for i in range(n):
    print(max(M[i] - a[i], a[i] - m[i]))
