# https://atcoder.jp/contests/past202012-open/tasks/past202012_o
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

n, m = map(int, input().split())

G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int1, input().split())
    G[a].append(b)
    G[b].append(a)

l = int(n**0.5)
def haveLF(i):
    return len(G[i]) > l

GC = [[] for _ in range(n)]
for i in range(n):
    for j in G[i]:
        if haveLF(j): GC[i].append(j)

R = [0] * n
P = [0] * n
S = [0] * n

q = int(input())
for _ in range(q):
    t, x = map(int1, input().split())
    if t == 0:
        if haveLF(x):
            P[x] += 1
        else:
            for nx in G[x]:
                R[nx] += 1
    else:
        ret = R[x]
        for nx in GC[x]:
            ret += P[nx]
        print(ret - S[x])
        S[x] = ret


#     print(R, P, S)
# print(G)
# print(GC)