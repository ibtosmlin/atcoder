# https://atcoder.jp/contests/s8pc-1/tasks/s8pc_1_b

from functools import cmp_to_key

def end(r=-1): print(r); exit()

def compare(item1, item2):
    """ "小さい" -> -1
        "等しい" -> 0
        "大きい" -> 1
    """
    # 以下はx, yが与えられてy/xで比較する例
    # y1/x1 < y2/x2
    # -> y1*x2 < y2*x1
    x1, y1 = item1
    x2, y2 = item2

    if y1*x2 < y2*x1:
        return -1
    elif y1*x2 > y2*x1:
        return 1
    else:
        return 0

def sort_by_function(x, compare):
    """比較関数を設定してソート
    """
    x.sort(key=cmp_to_key(compare))
    return x

h, w, n = map(int, input().split())
if n % 2:
    end(-1)

xy = []
for _ in range(n):
    xy.append(tuple(map(int, input().split())))

xy = sort_by_function(xy, compare)
l = xy[n//2-1]
r = xy[n//2]

if compare(l, r) == 0:
    end(-1)


ret = set()
for i in range(0, h+1):
    u = (w, i)
    if compare(l, u) == -1 and compare(u, r) == -1:
        ret.add(u)


for j in range(0, w+1):
    u = (j, h)
    if compare(l, u) == -1 and compare(u, r) == -1:
        ret.add(u)

if len(ret) == 0:
    end(-1)

ret = list(ret)
ret.sort()
for ri in ret:
    print(f'({ri[0]},{ri[1]})')
