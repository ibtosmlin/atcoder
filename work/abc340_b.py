l = []
for _ in range(int(input())):
    f, v = map(int, input().split())
    if f//2:
        print(l[-v])
    else:
        l.append(v)
