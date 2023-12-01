# https://atcoder.jp/contests/joi2011yo/tasks/joi2011yo_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n = int(input())
m = int(input())
d = n//2
tile = []
for _ in range(m):
    x, y = map(int, input().split())
    x -= d+1; y -= d+1
    u = max(abs(x), abs(y))
    u = (d+u)%3
    tile.append(u)
print(tile)