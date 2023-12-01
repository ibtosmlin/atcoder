# https://atcoder.jp/contests/joig2022-open/tasks/joig2022_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
N = int(input())
M = int(input())
PS = [[-1, 0]]
for a, v in [list(map(int, input().split())) for _ in range(N)]:
    if a == PS[-1][0]:
        PS[-1][1] = max(PS[-1][1], v)
    else:
        PS.append([a, v])
print(PS)