n, l = map(int, input().split())
k = int(input())
a = list(map(int, input().split()))

def isok(x):
    # スコア＝xが可能か
    # すべてのピースがx以上に分割・k個の切れ目
    # すべてのピースがx以上に分割していって、k個以上の切れ目になるか
    cnt = 0
    now = 0
    for i, ai in enumerate(a):
        if ai - now >= x:
            cnt += 1
            now = ai
    if l - now < x:
        cnt -= 1
    return cnt >= k

ng = 10**9
ok = 0

while ng - ok > 1:
    mid = (ng+ok)//2
    if isok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
