# https://atcoder.jp/contests/arc120/tasks/arc120_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1

n = int(input())
a = list(map(int, input().split()))
b = []
for i, ai in enumerate(a):
    b.append([ai, i, 0])
b.sort()
for i in range(n):
    b[i][2] = 1

b.sort(key=lambda x: x[1])

ret = [None] * (2*n)

now = -1
stack = []

for bi in b:
    if bi[-1] == now or now == -1:
        stack.append(bi)
        now = bi[-1]
    else:
        ret[bi[1]] = ")"
        x = stack.pop()
        ret[x[1]] = "("
        if len(stack) == 0:
            now = -1
#     print(now, stack)
# print(b)
# print(ret)
print(''.join(ret))