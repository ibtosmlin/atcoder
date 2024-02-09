# https://atcoder.jp/contests/abc335/tasks/abc335_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n, q = map(int, input().split())
que = []
for i in range(n, 0, -1):
    que.append((i, 0))

for _ in range(q):
    f, v = input().split()
    if f == '1':
        x, y = que[-1]
        if v == 'R':
            x += 1
        if v == 'L':
            x -= 1
        if v == 'U':
            y += 1
        if v == 'D':
            y -= 1
        que.append((x, y))
    else:
        print(*que[-int(v)])
