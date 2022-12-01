n, m = map(int, input().split())
a = list(map(int, input().split()))
ret = [m] * n
for ai in a:
    ret[ai-1] -= 1
print(*ret)