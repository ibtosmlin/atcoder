# https://atcoder.jp/contests/utpc2021/tasks/utpc2021_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1


from collections import deque
def swap(s, i, j):
    assert 0<= i < len(s)
    assert 0<= j < len(s)
    s = list(s)
    s[i], s[j] = s[j], s[i]
    return ''.join(s)

t = "UTPC"
l = len(t)
dist = {t: 0}
deq = deque([t])
while deq:
    x = deq.popleft()
    d = dist[x]
    for i in range(l):
        for j in range(i+1, l):
            nx = swap(x, i, j)
            if nx in dist: continue
            dist[nx] = d + 1
            deq.append(nx)

n = int(input())
s = input()

ret = 4
for i in range(n-3):
    x = s[i:i+4]
    for y, d in dist.items():
        for xj, yj in zip(x, y):
            if xj != yj: d += 1
        ret = min(ret, d)
print(ret)
