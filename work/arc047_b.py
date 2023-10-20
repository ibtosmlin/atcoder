# https://atcoder.jp/contests/arc047/tasks/arc047_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

INF = 10**10
N = int(input())
p = [tuple(map(int, input().split())) for _ in range(N)]
t = []
minu = INF; maxu = -INF
minv = INF; maxv = -INF

for x, y in p:
    u = x + y
    v = x - y
    t.append((u, v))
    minu = min(minu, u)
    maxu = max(maxu, u)
    minv = min(minv, v)
    maxv = max(maxv, v)

def iscenter(cu, cv):
    u, v = t[0]
    d = max(abs(cu - u), abs(cv - v))
    for u, v in t:
        if d != max(abs(cu - u), abs(cv - v)):
            return False
    return True

du = maxu-minu
dv = maxv-minv
D = max(du, dv)

ru= [maxu - D//2, minu + D//2]
rv = [maxv - D//2, minv + D//2]

# ru = maxu - D//2 or  minu + D//2
# rv = maxv - D//2 or  minv + D//2

for u in ru:
    for v in rv:
        if not iscenter(u, v): continue
        #print(u, v)
        print((u+v)//2, (u-v)//2)
        exit()
