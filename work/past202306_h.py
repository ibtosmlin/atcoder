# https://atcoder.jp/contests/past15-open/tasks/past202306_h
N = int(input())

def isok(x): # 1からxまでの和
    return x*(x+1)//2 <= N

ng = N+1
ok = 0
while ng-ok>1:
    mid = (ng+ok)//2
    if isok(mid):
        ok = mid
    else:
        ng = mid
print(ok)