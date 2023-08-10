from collections import defaultdict
n = int(input())
p = [0] * n
for _ in range(n*(n-1)//2):
    a, b, c, d = map(int, input().split())
    a -= 1; b -= 1
    if c > d:
        p[a] += 3
    elif c < d:
        p[b] += 3
    else:
        p[a] += 1
        p[b] += 1

pc = defaultdict(set)
for i in range(n):
    pc[p[i]].add(i)

ret = [-1] * n

cnt = 1
for k in sorted(pc.keys(), reverse=True):
    for v in pc[k]:
        ret[v] = cnt
    cnt += len(pc[k])

print("\n".join(map(str, ret)))