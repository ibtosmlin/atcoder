# https://atcoder.jp/contests/abc327/tasks/abc327_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

A = [list(map(int, input().split())) for _ in range(9)]
u = list(range(1, 10))

for i in range(9):
    if sorted(A[i]) != u: exit(print('No'))

for i in range(9):
    if sorted([A[j][i] for j in range(9)]) != u: exit(print('No'))

for i in range(3):
    for j in range(3):
        x = []
        for r in range(3):
            for s in range(3):
                x.append(A[i*3+r][j*3+s])
        # print(i,j,x)
        if sorted(x) != u: exit(print('No'))

print('Yes')