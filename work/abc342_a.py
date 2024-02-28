# https://atcoder.jp/contests/abc342/tasks/abc342_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
s = input()
from collections import Counter
c = Counter(s)
for k, v in c.items():
    if v == 1:
        u = k

for i in range(len(s)):
    if s[i] == u:
        print(i+1)