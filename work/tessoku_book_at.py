# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_at
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from datetime import datetime, timedelta
endtime = datetime.now() + timedelta(seconds = 0.8)
n = int(input())
A = [i%n for i in range(n+1)]
p = []
for _ in range(n):
    p.append(list(map(int, input().split())))

def dist(x, y):
    s, t = p[x]
    u, v = p[y]
    ret = (s - u) ** 2 + (t-v)**2
    return ret ** 0.5


def change(i):
    d = dist(A[i+1], A[i-1]) + dist(A[i], A[i+2])
    d -= dist(A[i], A[i-1]) + dist(A[i+1], A[i+2])
    return min(d, 0)

while datetime.now() < endtime:
    mi = 0
    switch = None
    for i in range(1, n-1):
        d = change(i)
        if mi > d:
            mi = min(mi, d)
            switch = i
    if switch:
        A[i], A[i+1] = A[i+1], A[i]

for ai in A:
    print(ai+1)