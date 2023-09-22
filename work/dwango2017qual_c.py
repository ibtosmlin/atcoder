# https://atcoder.jp/contests/dwacon2017-prelims/tasks/dwango2017qual_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from collections import deque

n = int(input())
a = [int(input()) for _ in range(n)]

ret = 0
vals = [deque([]) for _ in range(5)]

for i, ai in enumerate(a):
    vals[ai].append(i)

for i in range(n):
    ai = a[i]
    vals[ai].popleft()
    print(i, a, ai)
    if ai == 0: continue
    elif ai == 4:
        ret += 1
    elif ai == 3:
        ret += 1
        if len(vals[1]):
            x = vals[1].popleft()
            a[x] = 0
    elif ai == 2:
        ret += 1
        if len(vals[2]):
            x = vals[2].popleft()
            a[x] = 0
        elif len(vals[1]):
            x = vals[1].popleft()
            a[x] = 0
            if len(vals[1]):
                x = vals[1].popleft()
                a[x] = 0
    elif ai == 1:
        ret += 1
        if len(vals[3]):
            x = vals[3].popleft()
            a[x] = 0
        elif len(vals[2]):
            x = vals[2].popleft()
            a[x] = 0
            if len(vals[1]):
                x = vals[1].popleft()
                a[x] = 0
        elif len(vals[1]):
            x = vals[1].popleft()
            a[x] = 0
            if len(vals[1]):
                x = vals[1].popleft()
                a[x] = 0
                if len(vals[1]):
                    x = vals[1].popleft()
                    a[x] = 0

print(ret)

