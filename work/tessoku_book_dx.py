s = input()
que = []
ret = []
for i, si in enumerate(s):
    if si == '(':
        que.append(i)
    else:
        j = que.pop()
        ret.append((j+1, i+1))
for r in ret:
    print(*r)