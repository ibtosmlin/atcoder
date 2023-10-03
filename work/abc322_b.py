# https://atcoder.jp/contests/abc322/tasks/abc322_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, m = map(int, input().split())
s = input()
t = input()

if s == t[:n] and s == t[-n:]:
    exit(print(0))
if s == t[:n]:
    exit(print(1))
if s == t[-n:]:
    exit(print(2))
exit(print(3))
