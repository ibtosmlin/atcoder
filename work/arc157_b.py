# https://atcoder.jp/contests/arc157/tasks/arc157_b
# xの数 == kの時 n-1
# xの数 < kの時 n-1 - (k-x)
# xの数 > kの時
def end(r=-1):
    print(r)
    exit()


n, k = map(int, input().split())
s = list(input())
xcount = s.count('X')
if xcount == k:
    end(n-1)

from collections import deque
s = deque(s)

if xcount > k:
    # Yでうめるのみ
    hashi = 0
    while s[0] == 'X':
        hashi += 1
        s.popleft()
    while s[-1] == 'X':
        hashi += 1
        s.pop()
    kouho = []
    nowchar = 'Y'
    nowcount = 0
    for i, si in enumerate(s):
        if si == 'X':
            nowcount += 1
            nowchar = 'X'
        else:
            if nowchar == 'X':
                kouho.append(nowcount)
                nowcount = 0
                nowchar = 'Y'
    kouho.sort()
    ret = 0
    for ki in kouho:
        if ki <= k:
            ret += ki + 1
            k -= ki
        else:
            break
    ret += k
    end(ret)

else:
    # XをYでうめて残りk-xcount分を大きいところから削除
    hashi = 0
    while s[0] == 'Y':
        hashi += 1
        s.popleft()
    while s[-1] == 'Y':
        hashi += 1
        s.pop()
    kouho = []
    nowchar = 'X'
    nowcount = 0
    for i, si in enumerate(s):
        if si == 'Y':
            nowcount += 1
            nowchar = 'Y'
        else:
            if nowchar == 'Y':
                kouho.append(nowcount)
                nowcount = 0
                nowchar = 'X'
    k -= xcount
    if hashi >= k:
        end(n-1-k)
    else:
        k -= hashi
        kouho.sort(reverse=True)
        ret = n - 1 - hashi
        for ki in kouho:
            if ki <= k:
                ret -= ki + 1
                k -= ki
            else:
                break
        if k > 0:
            ret -= k+1
        end(ret)


