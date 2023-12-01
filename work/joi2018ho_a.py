# https://atcoder.jp/contests/joi2018ho/tasks/joi2018ho_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n, k = map(int, input().split())
T = []
for _ in range(n):
    t = int(input())
    T.append(t)
D = []
for i in range(n-1):
    D.append(T[i+1] - T[i] - 1)
D.sort()
print(n + sum(D[:n-k]))
