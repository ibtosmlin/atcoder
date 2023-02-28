n, a, b, c, d = map(int, input().split())
if b == 0 and c == 0:
    ret = a == n-1 or d == n-1
else:
    ret = abs(b - c) <= 1
print('Yes' if ret else 'No')