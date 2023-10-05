# https://atcoder.jp/contests/abc320/tasks/abc320_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from heapq import heapify, heappop, heappush

n, m = map(int, input().split())
que = []
event = []
ret = [0] * n
hq = []
mt = 0
for _ in range(m):
    t, w, s = map(int, input().split())
    heappush(hq, (t*10+1, (w, s)))
    mt = max(mt, t+s)
for x in range(n):
    heappush(hq, (0, (x, 0)))

while hq:
    t, (w, s) = heappop(hq)
    t, f = divmod(t, 10)
    if f == 0:
        heappush(que, w)
    else:
        if que:
            x = heappop(que)
            ret[x] += w
            if t+s <= mt:
                heappush(hq, ((t+s)*10, (x, 0)))
        m -= 1
    if m == 0: break

print('\n'.join(map(str, ret)))