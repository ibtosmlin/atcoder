# https://atcoder.jp/contests/abc255/tasks/abc255_f
import sys
sys.setrecursionlimit(10001000)
def end(r=-1): print(r); exit()

n = int(input())
P = list(map(int, input().split()))
I = list(map(int, input().split()))

if P[0] != 1: end(-1)

posI = {ai:i for i, ai in enumerate(I)}
ret = [[0] * 2 for _ in range(n+1)]

def dfs(pl=0, pr=n, il=0, ir=n):
    # print(P[pl:pr], I[il:ir])
    r = P[pl]
    posr = posI[r]
    if not (il <= posr < ir): end(-1)
    if posr != il:   # left exists
        _il, _ir = il, posr
        _pl = pl+1
        _pr = _pl + (_ir - _il)
        ret[r][0] = P[_pl]
        dfs(_pl, _pr, _il, _ir)
    if posr != ir-1:   # right exists
        _il, _ir = posr+1, ir
        _pr = pr
        _pl = _pr - (_ir - _il)
        ret[r][1] = P[_pl]
        dfs(_pl, _pr, _il, _ir)

dfs()

for ri in ret[1:]:
    print(*ri)