# https://atcoder.jp/contests/abc328/tasks/abc328_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, q= map(int, input().split())
s = input()
C = [0] * (n+1)
for i in range(n-1):
    if s[i] == s[i+1]:
        C[i+1] += 1
for i in range(n):
    C[i+1] += C[i]

for _ in range(q):
    l, r = map(int1, input().split())
    print(C[r]-C[l])
