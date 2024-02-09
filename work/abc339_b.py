h, w, n = map(int, input().split())
direc = [(-1, 0), (0, 1), (1, 0), (0, -1)]
G = [["."] * w for _ in range(h)]
i = 0; j = 0; d = 0
for _ in range(n):
    if G[i][j] == ".":
        G[i][j] = "#"
        d += 1
    else:
        G[i][j] = "."
        d -= 1
    d %= 4
    i = (i + direc[d][0])%h
    j = (j + direc[d][1])%w
for gi in G:
    print("".join(gi))