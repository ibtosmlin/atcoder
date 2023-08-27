# https://atcoder.jp/contests/past202209-open/tasks/past202209_l
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

n, m = map(int, input().split())
A = list(map(int, input().split()))
