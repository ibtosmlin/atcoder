# https://atcoder.jp/contests/abc320/tasks/abc320_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

ret = 0
s = input()
n = len(s)
for l in range(n):
    for r in range(l+1, n+1):
        t = s[l:r]
        if t == t[::-1]:
            ret = max(ret, r-l)
print(ret)