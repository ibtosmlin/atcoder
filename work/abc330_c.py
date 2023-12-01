# https://atcoder.jp/contests/abc330/tasks/abc330_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
d = int(input())
ret = 10**20
for x in range(int(d**0.5)+1):
    y = int(abs(d - x**2)**0.5)
    ret = min(ret, abs(x ** 2 + y**2 - d))
    ret = min(ret, abs(x ** 2 + (y+1)**2 - d))
print(ret)