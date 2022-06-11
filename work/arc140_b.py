import heapq

n = int(input())
s = input()

a = [0] * n
c = [0] * n

nw = 0
for i, si in enumerate(s):
    if si == 'A':
        nw += 1
        continue
    if si == 'R':
        a[i] = nw
    nw = 0

nw = 0
for i, si in enumerate(s[::-1]):
    if si == 'C':
        nw += 1
        continue
    if si == 'R':
        c[i] = nw
    nw = 0

c = c[::-1]

b = []
heapq.heapify(b)
single = 0

for ai, ci in zip(a, c):
    r = min(ai, ci)
    if r == 1:
        single += 1
    if r > 1:
        heapq.heappush(b, r)

ret = 0
while True:
    if ret%2 == 0:
        if len(b) > 0:
            x = heapq.heappop(b)
            x -= 1
            if x == 1:
                single += 1
            else:
                heapq.heappush(b, x)
        else:
            if single > 0:
                single -= 1
            else:
                break
    else:
        if single > 0:
            single -= 1
        else:
            if len(b) > 0:
                heapq.heappop(b)
            else:
                break
    ret += 1


print(ret)
