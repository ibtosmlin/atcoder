

n = int(input())
a = list(map(int, input().split()))

for i, ai in enumerate(a):
    a[:i]