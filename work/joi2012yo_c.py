n = int(input())
A, B = map(int, input().split())
C = int(input())
T = [int(input()) for _ in range(n)]
T.sort(reverse=True)

ret = C // A
for ti in T:
    C += ti
    A += B
    ret = max(ret, C // A)
print(ret)
