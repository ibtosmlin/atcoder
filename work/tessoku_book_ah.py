n, x, y = map(int, input().split())

grundy = [0] * 100010
for i in range(x, 100010):
    used = []
    for j in [x, y]:
        nxt = i - j
        if nxt < 0: continue
        used.append(grundy[nxt])
    while grundy[i] in used:
        grundy[i] += 1

A = list(map(int, input().split()))
nim = 0
for ai in A:
    nim ^= grundy[ai]
if nim:
    print('First')
else:
    print('Second')
