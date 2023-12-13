# https://atcoder.jp/contests/past15-open/tasks/past202306_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

N, K = map(int, input().split())
a = list(map(int, input().split()))
ret = 0
# N-1 K-1選ぶ
C = 1
for i in range(1, K):
    C *= (N-i)
for i in range(1, K):
    C //= i
print(C*sum(a))
