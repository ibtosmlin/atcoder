m, n = map(int, input().split())

isok = []
for i in range(1<<m):
    fg = True
    for j in range(m):
        bitj = i >> j & 1
        bitjn = i >> (j+1) & 1
        if bitj == 1 and bitnj == 1:
            fg = False
    if fg: isok.append(i)

for biti in isok:
    for bitj in isok:
