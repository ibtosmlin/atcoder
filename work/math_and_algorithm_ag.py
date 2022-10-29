def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])
def distPtoP(pt1, pt2): return dist2(pt1, pt2) ** 0.5
def distCtoC(c1, c2):
    pt1, r1 = c1; pt2, r2 = c2; R, r, d = max(r1, r2), min(r1, r2), distPtoP(pt1, pt2)
    if d > R+r:
        return 5
    elif d == R+r:
        return 4
    elif d < R - r:
        return 1
    elif d == R - r:
        return 2
    else:
        return 3
    # d > R+r :O o
    # d < R-r: ◎
    # else 交差


x, y, r = map(int, input().split())
c1 = ((x, y), r)
x, y, r = map(int, input().split())
c2 = ((x, y), r)

print(distCtoC(c1, c2))