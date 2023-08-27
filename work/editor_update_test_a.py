# https://atcoder.jp/contests/editor-update-test/tasks/editor_update_test_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

t = int(input())
for _ in range(t):
    n, a, b, c = map(int, input().split())
    for i in range(n+1):
        for j in range(n+1):
            