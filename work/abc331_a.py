# https://atcoder.jp/contests/abc331/tasks/abc331_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
M, D = map(int, input().split())
y, m, d = map(int, input().split())

d += 1

if d == D+1:
    d = 1
    m += 1
if m == M+1:
    m = 1
    y += 1
print(y, m, d)
