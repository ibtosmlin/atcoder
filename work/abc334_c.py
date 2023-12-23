# https://atcoder.jp/contests/abc334/tasks/abc334_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1


N, K = map(int, input().split())
A = list(map(int1, input().split()))

L = [0]
for i in range(0, K-1, 2):
    L.append(L[-1] + A[i+1] - A[i])
R = [0]
for i in range(K-1, 0, -2):
    R.append(R[-1] + A[i] - A[i-1])
R = R[::-1]
if K == 1 or K%2 == 0:
    exit(print(L[-1]))

ret = 10**10
for l, r in zip(L, R):
    ret = min(l+r, ret)
print(ret)