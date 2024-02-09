# https://atcoder.jp/contests/abc338/tasks/abc338_e
import sys; input: lambda _: sys.stdin.readline().rstrip()

n = int(input())
u = [-1] * (2*n)
for i in range(n):
    a, b = map(lambda x: int(x)-1, input().split())
    if a > b: a, b = b, a
    u[a] = u[b] = i

stack = []
for ui in u:
    if stack and stack[-1] == ui:
        stack.pop()
    else:
        stack.append(ui)

print('Yes' if stack else 'No')
