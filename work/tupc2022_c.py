# https://atcoder.jp/contests/tupc2022/tasks/tupc2022_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

h, w, n = map(int, input().split())
pt = set()
for _ in range(n):
    x,y = map(int1, input().split())
    pt.add((x, y))

ret = set()
direc = {(1, 0), (0, 1), (1, 1), (0, 0)}

def isok(x, y):
    u = 0
    for dx, dy in direc:
        if (x+dx,y+dy) in pt: u += 1
    return u%2


for x, y in pt:
    for dx, dy in direc:
        nx = x-dx
        ny = y-dy
        if nx >= 0 and ny >= 0 and isok(nx, ny):
            ret.add((nx, ny))

print(len(ret))
