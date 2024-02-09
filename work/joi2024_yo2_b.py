# https://atcoder.jp/contests/joi2024yo2/tasks/joi2024_yo2_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

N, M, Q = map(int, input().split())

C = [0] * 200100
