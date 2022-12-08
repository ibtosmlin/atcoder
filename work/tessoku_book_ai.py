import sys
sys.setrecursionlimit(10**9)
n = int(input())
A = list(map(int, input().split()))

for i in range(n)[::-1]:
    for j in range(i):
        if i%2==0:  #最小化
            A[j] = min(A[j:j+2])
        else:   #最大化
            A[j] = max(A[j:j+2])
print(A[0])
