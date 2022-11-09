def end(r=-1): print(r); exit()
INF = float('inf')
a, k = input().split()
k = int(k)
ia = int(a)
a = list(a)
n = len(a)
if k == 10: end(0)
if k == 1:
    ret = ia
    for i in range(1, n+1):
        for j in range(10):
            u = str(j) * i
            u = int(u)
            ret = min(ret, abs(u - ia))
    end(ret)

# A[:x] + Q + R[n:]
def diff(pi, q, r):
    u = a[:]
    u[pi] = str(q)
    u[pi+1:] = str(r) * (n - pi - 1)
    if u[0] == '0': return ia
    if len(set(u)) > k: return ia
    u = int(''.join(u))
    return abs(u - ia)


ret = ia
for pi in range(len(a)):
    for q in range(10):
        for r in range(10):
            nw = diff(pi, q, r)
            ret = min(ret, nw)

print(ret)
