# https://atcoder.jp/contests/abc143/tasks/abc143_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
s = input() + "#"
ret = 0
nw = s[0]
for si in s:
    if nw == si: continue
    nw = si
    ret += 1
print(ret)