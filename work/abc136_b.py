# https://atcoder.jp/contests/abc136/tasks/abc136_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

n = int(input())
ret = 0
for i in range(1, n+1):
    if len(str(i))%2:
        ret += 1
print(ret)