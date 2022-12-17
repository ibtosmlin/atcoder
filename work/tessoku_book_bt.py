h, w, k = map(int, input().split())
G = [[0] * w for _ in range(h)]
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == '#':
            G[i][j] = 1

def f(s):
    bitcount = 0
    notselrow = []
    ret = 0
    for i in range(h):
        if s >> i & 1 == 0:
            notselrow.append(i)
        else:
            bitcount += 1
    if bitcount > k: return 0
    ret += w * bitcount
    tate = [0] * w
    for i in notselrow:
        for j in range(w):
            tate[i] += G[i][j]
    tate.sort()
    for i in range(k-bitcount):
        tate[i] = len(notselrow)
    return ret + sum(tate)

ret = 0
for s in range(1<<h):
    ret = max(ret, f(s))
print(ret)