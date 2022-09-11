from collections import defaultdict
n = int(input())
p = list(map(int, input().split()))

pos = [-1] * n
for i, pi in enumerate(p):
    pos[pi] = i

d = defaultdict(int)
for i, posi in enumerate(pos):
    for u in [-1, 0, 1]:
        d[(i - posi + u)%n] += 1

print(max(d.values()))
