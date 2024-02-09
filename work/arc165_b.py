# https://atcoder.jp/contests/arc165/tasks/arc165_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from sortedcontainers import SortedSet

N, K = map(int, input().split())
A = list(map(int, input().split()))

change = []
for i in range(N):
    if A[i] < A[i+1]: continue
    change.append()

S = SortedSet()
cnt = 0
for i in range(N)[::-1]:
    S.add(A[i])
    cnt += 1
    if cnt < K: continue
    if cnt > K:
        S.remove(A[i+K])
        cnt -= 1
    if S[0] == A[i]:
        while i-1 >= 0 and A[i-1] < A[i]:
            i -= 1
        print(" ".join(map(str, A[:i] + sorted(A[i:i+K]) + A[i+K:])))
        exit()
print(*A)