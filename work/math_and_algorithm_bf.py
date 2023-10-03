# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_bf
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
line = [tuple(map(int, input().split())) for _ in range(n)]

ret = 0
for i in range(n):
    a1, b1, c1 = line[i]
    for j in range(i):
        a2, b2, c2 = line[j]
        d = a1*b2-a2*b1
        if d == 0: continue
        x = (c1*b2 - c2*b1) / d
        y = (c2*a1 - c1*a2) / d
        for k in range(n):
            a3, b3, c3 = line[k]
            if a3 * x + b3 * y > c3: break
        else:
            ret = max(ret, x+y)
print(ret)