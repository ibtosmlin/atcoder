# https://atcoder.jp/contests/arc142/tasks/arc142_c
n = int(input())
nei = [[] for _ in range(3)]
for i in range(1, n+1):
    for j in range(1, 3):
        if i+j <= 3: continue
        print(f'? {i} {j}', flush=True)
        di = int(input())
        if di == 1:
            nei[j].append(i)

if len(nei[1]) == 0 or len(nei[2]) == 0:
    ret = 1
    print(ret); exit()
if len(nei[1]) == 1 and len(nei[2]) == 1:
    print(f'? {nei[1][0]} {nei[2][0]}', flush=True)
    d = int(input())
    print(f'? {nei[1][0]} 2', flush=True)
    d2 = int(input())
    print(f'? {nei[2][0]} 1', flush=True)
    d1 = int(input())
    if d == 3 and d2 == 2 and d1 == 2:
        ret = 1
        print(ret); exit()

ret = n
for i in nei[1]:
    for j in nei[2]:
        print(f'? {i} {j}', flush=True)
        di = int(input())
        ret = min(ret, di)

print(f'! {ret+2}', flush=True)

