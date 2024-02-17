l = []
for _ in range(int(input())):
    f, v = input().split()
    if f != "1": print(l[-int(v)])
    else: l.append(v)
