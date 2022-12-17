n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

rows = {i:i for i in range(n)}
q = int(input())
for _ in range(q):
    f, x, y = map(int, input().split())
    x -= 1; y -= 1
    if f == 1:
        rows[x], rows[y] = rows[y], rows[x]
    else:
        print(a[rows[x]][y])