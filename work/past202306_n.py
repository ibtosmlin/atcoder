# https://atcoder.jp/contests/past15-open/tasks/past202306_n
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n, m = map(int, input().split())
C = list(map(int, input().split()))
