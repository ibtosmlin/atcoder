# https://atcoder.jp/contests/codequeen2023-final-open/tasks/codequeen2023_final_d
import sys
from collections import defaultdict
def input(): return sys.stdin.readline().rstrip()
def isin(x, y): return (0<= x < R) and (0<= y < C)
R, C , rs, cs, rt, ct = map(int, input().split())

direc = {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1) (-1, 1), (-1, -1)}

rconst = defaultdict(int)
cconst = defaultdict(int)
pconst = dd = defaultdict(int)
mconst = dd = defaultdict(int)

for d in range(1, max(R, C)+1):
    for rd, cd in direc:
        nr, nc = rs + rd * d, cs + cd * d
        




