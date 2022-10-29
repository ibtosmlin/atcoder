n = int(input())
ret = [True] * (n+1)
ret[0] = False
ret[1] = False
ans = []
for i in range(2, n+1):
    if ret[i] == False: continue
    ans.append(i)
    for pi in range(i*2, n+1, i):
        ret[pi] = False
print(*ans)