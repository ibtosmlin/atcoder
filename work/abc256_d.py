n = int(input())
k = [0] * 200010
for i in range(n):
    l, r = map(int, input().split())
    k[l] += 1
    k[r] -= 1

for i in range(1, 200010):
    k[i] += k[i-1]

ls = []
rs = []
for i in range(1, 200010):
    if k[i-1] == 0 and k[i] != 0:
        ls.append(i)
    if k[i-1] != 0 and k[i] == 0:
        rs.append(i)

for l, r in zip(ls, rs):
    print(l, r)
