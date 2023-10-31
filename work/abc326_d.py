# https://atcoder.jp/contests/abc326/tasks/abc326_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

from itertools import permutations, product

n = int(input())
R = input()
C = input()
pt = product(permutations(range(n)), repeat = 3)
for a, b, c in pt:
    if any(ai == bi or bi == ci or ci == ai for ai, bi, ci in zip(a, b, c)): continue
    ret = [['.'] * n for _ in range(n)]
    for i, j in enumerate(a): ret[i][j] = 'A'
    for i, j in enumerate(b): ret[i][j] = 'B'
    for i, j in enumerate(c): ret[i][j] = 'C'
    _R = ['.'] * n
    _C = ['.'] * n
    for i in range(n):
        for j in range(n):
            s = ret[i][j]
            if s == '.': continue
            if _R[i] != '.': continue
            _R[i] = s
    if ''.join(_R) != R: continue
    for j in range(n):
        for i in range(n):
            s = ret[i][j]
            if s == '.': continue
            if _C[j] != '.': continue
            _C[j] = s
    if ''.join(_C) != C: continue
    print('Yes')
    for ri in ret:
        print(''.join(ri))
    exit()
print('No')
