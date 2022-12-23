# https://atcoder.jp/contests/past202012-open/tasks/past202012_k
import sys
from functools import lru_cache
sys.setrecursionlimit(10001000)
S = ''.join([input() for _ in range(4)])
x = [0, 1, 0, -1, 0]
y = [0, 0, 1, 0, -1]

# E = 1 + (s + c*E)/5
# E = (5 + s) /(5-c)

def toList(S):
    ret = [[None] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            ret[i][j] = S[4*i+j]
    return ret

def toStr(s):
    return ''.join([''.join(si) for si in s])


@lru_cache(maxsize=None)
def dfs(T):
    t = toList(T)
    if T == '.' * 16: return 0
    ret = 10**10
    for i in range(4):
        for j in range(4):
            sm, c = 0, 0
            for k in range(5):
                di = i + x[k]
                dj = j + y[k]
                if not (0<=di<4 and 0<=dj<4):
                    c += 1
                elif t[di][dj] == '.':
                    c += 1
                else:
                    t[di][dj] = '.'
                    sm += dfs(toStr(t))
                    t[di][dj] = '#'
            if c == 5: continue
            e = (5+sm) / (5-c)
            ret = min(e, ret)
    return ret

print(dfs(S))
