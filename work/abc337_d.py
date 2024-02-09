# https://atcoder.jp/contests/abc337/tasks/abc337_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

h, w, k = map(int, input().split())
Gw = [[0] * w for _ in range(h)]
Gh = [[0] * h for _ in range(w)]
INF = 10**20

for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == 'x':
            Gw[i][j] = -INF
            Gh[j][i] = -INF
        if s[j] == 'o':
            Gw[i][j] = 1
            Gh[j][i] = 1

def solv(G, h, w):
    ret = -INF
    for i in range(h):
        if w < k: continue
        now = sum(G[i][:k])
        ret = max(ret, now)
        for j in range(w):
            if j+k == w: break
            now -= G[i][j]
            now += G[i][j+k]
            ret = max(ret, now)
    return ret

ret = max(solv(Gw, h, w), solv(Gh, w, h))

if ret < 0:
    print(-1)
else :
    print(k-ret)