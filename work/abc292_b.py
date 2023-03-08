n, q = map(int, input().split())
num = [0] * (n+1)
for _ in range(q):
    f, x = map(int, input().split())
    if f != 3:
        num[x] += f
    else:
        ret = num[x] >= 2
        print('Yes' if ret else 'No')
