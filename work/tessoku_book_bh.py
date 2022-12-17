n = int(input())
a = list(map(int, input().split()))
stack = []
ret = []
for i, ai in enumerate(a):
    while stack and a[stack[-1]] <= ai:
        stack.pop()
    if stack:
        ret.append(stack[-1] + 1)
    else:
        ret.append(-1)
    stack.append(i)
print(*ret)