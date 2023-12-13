# https://atcoder.jp/contests/past15-open/tasks/past202306_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
a = list(map(int, input().split()))
b = []
for i, ai in enumerate(a):
    b.append((ai, i))
b.sort()
for i in range(n):
    _, j = b[i]
    a[j] = i+1
print(*a)
