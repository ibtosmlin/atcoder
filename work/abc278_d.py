n = int(input())
a = list(map(int, input().split()))
d = dict()
for i in range(n):
    d[i] = a[i]

base = None

q = int(input())
for i in range(q):
    que = list(map(int, input().split()))
    if que[0] == 1:
        d = dict()
        base = que[1]
    elif que[0] == 2:
        id = que[1] - 1
        x = que[2]
        if id in d:
            d[id] += x
        else:
            d[id] = base + x
    else:
        id = que[1] - 1
        if id in d:
            print(d[id])
        else:
            print(base)
