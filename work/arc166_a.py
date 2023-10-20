# https://atcoder.jp/contests/arc166/tasks/arc166_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from collections import deque

def isok(x, y):
    n = len(x)
    da, db = 0, 0
    for i in range(n):
        if y[i] == 'A': da += 1
        if y[i] == 'B': db += 1
        if x[i] == 'A': da -= 1
        if x[i] == 'B': db -= 1
    if da < 0 or db < 0: return False
    for i in range(n):
        if x[i] != 'C': continue
        if da:
            da -= 1; x[i] = 'A'
        elif db:
            db -= 1; x[i] = 'B'

    que = deque([i for i in range(n) if x[i] == 'B'])

    for i in range(n):
        if x[i] == 'B':
            que.popleft()
            if y[i] == 'A': return False
        else:
            if y[i] == 'B':
                j = que.popleft()
                x[i], x[j] = 'B', 'A'
    return True

def solve():
    n, x, y = input().split()
    n = int(n) + 1
    x = list(x); y = list(y)
    x.append('C'); y.append('C')
    prev = -1
    xs, ys = [], []
    for i in range(n):
        if y[i] != 'C': continue
        if y[i] == 'C' and x[i] != 'C': return False
        xs.append(x[prev+1:i])
        ys.append(y[prev+1:i])
        prev = i
    for xsi, ysi in zip(xs, ys):
        if not xsi: continue
        if not isok(xsi, ysi): return False
    return True

t = int(input())
for _ in range(t):
    print('Yes' if solve() else 'No')
