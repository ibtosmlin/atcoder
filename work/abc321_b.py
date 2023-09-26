# https://atcoder.jp/contests/abc321/tasks/abc321_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, x = map(int, input().split())
A = list(map(int, input().split()))
s = sum(A)
mn = min(A)
mx = max(A)

def scal(i): return s + i - min(mn, i) - max(mx, i)

for i in range(0, 101):
    if scal(i) >= x: exit(print(i))
print(-1)


