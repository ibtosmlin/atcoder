n = int(input())
sparse = dict()
sparselist = []
m = 0
width = [1]
while True:
    w = width[-1] * 2
    if w > n: break
    width.append(w)

sparse = []
for l in range(1, n+1):
    for w in width:
        r = l+w-1
        if r <= n:
            sparse.append((l, r))
        else:
            break

sparseindex = dict()
for i, lr in enumerate(sparse):
    sparseindex[lr] = i+1

print(len(sparseindex), flush=True)
for l, r in sparseindex:
    print(l, r, flush=True)

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    d = 1
    lr = l + d - 1
    rl = r - d + 1
    while lr < rl:
        d *= 2
        lr = l + d - 1
        rl = r - d + 1

    lc = sparseindex[(l, lr)]
    rc = sparseindex[(rl, r)]
    print(lc, rc, flush=True)
