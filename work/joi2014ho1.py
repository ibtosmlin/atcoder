# https://atcoder.jp/contests/joi2014ho/tasks/joi2014ho1
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]
r = [list(input()) for _ in range(2)]

def check(i, j):
    if i+1 >= n or j+1 >= m: return False
    for u in range(2):
        for v in range(2):
            if s[i+u][j+v] != r[u][v]: return False
    return True

def checkr(i, j):
    ret = 0
    for u in range(2):
        for v in range(2):
            if check(i-u, j-v):
                ret += 1
    return ret

ret = 0
for i in range(n):
    for j in range(m):
        if check(i,j):
            ret += 1

diff = 0
for i in range(n):
    for j in range(m):
        _sij = s[i][j]
        d = 0
        for rstr in 'JOI':
            if rstr == _sij: continue
            s[i][j] = rstr
            d = max(d, checkr(i, j))
        s[i][j] = _sij
        d -= checkr(i, j)
        diff = max(diff, d)

print(ret + diff)