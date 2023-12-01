# https://atcoder.jp/contests/abc143/tasks/abc143_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
a = list(map(int, input().split()))
ret = 0
for i in range(n):
    for j in range(i):
        ret += a[i]*a[j]
print(ret)
