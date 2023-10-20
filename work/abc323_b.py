# https://atcoder.jp/contests/abc323/tasks/abc323_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
s = [input() for _ in range(n)]

ret = []
for i in range(n):
    win = s[i].count('o')
    ret.append((-win, i+1))


ret.sort()
print(*[i for _, i in ret])
