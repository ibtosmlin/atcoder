# https://atcoder.jp/contests/abc167/tasks/abc167_f
n = int(input())
pos = []
neg = []
for _ in range(n):
    s = input()
    nw = 0
    mn = 0
    for si in s:
        if si == '(':
            nw += 1
        else:
            nw -= 1
        mn = min(mn, nw)
    if nw >= 0:
        pos.append((mn, nw))
    else:
        nw = 0
        mn = 0
        for si in s[::-1]:
            if si == ')':
                nw += 1
            else:
                nw -= 1
            mn = min(mn, nw)
        neg.append((mn, nw))


pos.sort(reverse=True)
neg.sort(reverse=True)


lnw = 0
for mn, d in pos:
    if lnw + mn < 0:
        print('No')
        exit()
    lnw += d

rnw = 0
for mn, d in neg:
    if rnw + mn < 0:
        print('No')
        exit()
    rnw += d

print('Yes' if lnw == rnw else 'No')