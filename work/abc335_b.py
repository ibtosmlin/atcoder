# https://atcoder.jp/contests/abc335/tasks/abc335_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n = int(input())
ret = []
for x in range(100):
    for y in range(100):
        for z in range(100):
            if x+y+z <= n:
                print(x, y, z)
