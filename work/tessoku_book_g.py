d = int(input())
n = int(input())
A = [0] * (d+1)
for _ in range(n):
    l, r = map(int, input().split())
    l -= 1
    A[l] += 1
    A[r] -= 1
for i in range(1, d+1):
    A[i] += A[i-1]

print(*A[:-1])