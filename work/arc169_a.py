# https://atcoder.jp/contests/arc169/tasks/arc169_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n = int(input())
A = list(map(int, input().split()))
P = [-1] + list(map(int1, input().split()))
D = [-1] * n
D[0] = 0
for i in range(1, n):
    D[i] = D[P[i]] + 1

S = [0] * (max(D)+1)
for i in range(n):
    S[D[i]] += A[i]

ret = "0"
for si in reversed(S):
    if si == 0: continue
    ret = "-+"[si>0]
    break
print(ret)
