# https://atcoder.jp/contests/abc332/tasks/abc332_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n, s ,k = map(int, input().split())
ret = 0
for _ in range(n):
    p, q = map(int, input().split())
    ret += p*q
if ret < s:
    ret += k
print(ret)