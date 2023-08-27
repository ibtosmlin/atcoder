# https://atcoder.jp/contests/past202209-open/tasks/past202209_n
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1
from collections import deque

h, w, q = map(int, input().split())
S = [tuple(input()) for _ in range(h)]
transpose = h > w
if transpose:
    h, w = w, h
    S = list(zip(*S))

dat = [deque(si) for si in S]

ret = []
for _ in range(q):
    f, p, c = input().split()
    f = int1(f)
    p = int1(p)
    if transpose: f = 1 - f
    if f == 0:
        ret.append(dat[p].pop())
        dat[p].appendleft(c)
    else:
        ret.append(dat[-1][p])
        for i in range(h-1, 0, -1):
            dat[i][p] = dat[i-1][p]
        dat[0][p] = c

print(''.join(ret))