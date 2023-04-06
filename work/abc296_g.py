# https://atcoder.jp/contests/abc296/tasks/abc296_g
# cross product: (b - a)×(c - a)
def cross3(a, b, c):
    return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])

# O(log N)
def inside_convex_polygon(p0, qs):
    EPS = 1e-10
    L = len(qs)
    left = 1; right = L
    q0 = qs[0]
    while left+1 < right:
        mid = (left + right) >> 1
        if cross3(q0, p0, qs[mid]) <= 0:
            left = mid
        else:
            right = mid
    if left == L-1:
        left -= 1
    qi = qs[left]; qj = qs[left+1]
    v0 = cross3(q0, qi, qj)
    v1 = cross3(q0, p0, qj)
    v2 = cross3(q0, qi, p0)
    if v0 < 0:
        v1 = -v1; v2 = -v2
    if 0 <= v1 and 0 <= v2 and v1 + v2 <= v0:
        if left == 1 and abs(v2) < EPS:
            return "ON"
        if left + 1 == L - 1 and abs(v1) < EPS:
            return "ON"
        if abs(v1 + v2 - v0) < EPS:
            return "ON"
        return "IN"
    return "OUT"

n = int(input())
qs = [tuple(map(int,input().split())) for _ in range(n)]
q = int(input())
for _ in range(q):
    x = tuple(map(int,input().split()))
    ret = inside_convex_polygon(x, qs)
    print(ret)