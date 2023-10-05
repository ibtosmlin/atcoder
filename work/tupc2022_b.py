# https://atcoder.jp/contests/tupc2022/tasks/tupc2022_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, m, k = map(int, input().split())
event = [(0,0)]
for _ in range(m):
    a, b = map(int, input().split())
    event.append((a, b))
event.append((n+1, 0))
N = len(event)

ret = 0
h = 0
for i in range(N-1):
    # print(i, "A", h, event[i], event[i+1])
    d0, ha = event[i]
    d1, _ = event[i+1]
    h += ha
    ret += min(d1-d0, max(0, h-k))
    h -= d1 -d0
    h = max(h, 0)
    # print(i, "B", h, "ret:",ret)

print(ret)