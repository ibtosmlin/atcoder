n, s = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) < s:
    print(0)
    exit()

def isok(m):
    x = sum(a[:m])
    if x >= s: return True
    for i in range(n-m):
        x -= a[i]
        x += a[i+m]
        if x >= s: return True
    return False

ok = n
ng = 0
while ok - ng > 1:
    mid = (ok + ng) // 2
    if isok(mid):
        ok = mid
    else:
        ng = mid
print(ok)