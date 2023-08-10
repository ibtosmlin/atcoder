n = int(input())
a = list(map(int, input().split()))
a.sort()
s = sum(a)
x0, c1 = divmod(s, n)
x1 = x0+1
c0 = n-c1
b = [x0] * c0 + [x1] * c1

ret=0
for ai, bi in zip(a, b):
    ret += abs(ai-bi)
print(ret//2)