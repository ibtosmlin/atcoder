# https://atcoder.jp/contests/abc321/tasks/abc321_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
rb = [0]
for i in range(m):
    rb.append(rb[-1] + b[i])
ret = 0
j = m
for i in range(n):
    while j > 0 and b[j-1] + a[i] >= p:
        j -= 1
    # a[i] + b[j] <= p
    ret += rb[j] + j * a[i] + (m-j) * p

print(ret)
