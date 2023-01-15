def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])
def distPtoP(pt1, pt2): return dist2(pt1, pt2) ** 0.5
x1, y1, x2, y2 = map(int, input().split())
pt1 = (x1, y1)
pt2 = (x2, y2)
q = int(input())
for _ in range(q):
    pt = tuple(map(int, input().split()))
    d = distPtoP(pt1, pt)
