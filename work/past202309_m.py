# https://atcoder.jp/contests/past16-open/tasks/past202309_m
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

import math
EPS = 1e-08
MAX = 2e09
PI = math.pi

######################################################################
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)

    def __mul__(self, const):
        return Point(self.x * const, self.y * const)

    def __truediv__(self, const):
        return Point(self.x / const, self.y / const)

    def __eq__(self, other):
        return (self - other).norm2 < EPS

    @property
    def norm2(self):
        return self.x **2 + self.y **2

    @property
    def abs(self):
        return self.norm2 ** 0.5

    @property
    def radian(self):
        return math.atan2(self.y, self.x)

    @property
    def quadrant(self):
        if self.x == 0 and self.y == 0: return 0
        if self.x > 0 and self.y >= 0: return 1
        if self.x <= 0 and self.y > 0: return 2
        if self.x < 0 and self.y <= 0: return 3
        return 4

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def det(self, other):
        return self.x * other.y - self.y * other.x

    def dot3(self, other1, other2):
        return (other1 - self).dot(other2 - self)

    def det3(self, other1, other2):
        return (other1 - self).det(other2 - self)

    def dist2(self, other):
        d = self - other
        return (d.x)**2 + (d.y)**2

    def dist(self, other):
        return self.dist2(other) ** 0.5

    def __lt__(self, other):
        seq = self.quadrant
        otq = other.quadrant
        det = self.det(other)
        if seq != otq:
            return seq < otq
        if det == 0:
            return self.norm2 < other.norm2
        else:
            return det > 0

    def rotate_radian(self, rad):
        cos, sin = math.cos(rad), math.sin(rad)
        return Point(self.x * cos - self.y * sin, self.x * sin + self.y * cos)

    def rotate_degree(self, rad):
        rad = math.radians(rad)  # radが度数の場合
        return self.rotate_radian(rad)

    @property
    def orthogonal(self):
        return Point(- self.y, self.x)

    def counter_clockwise(self, other1, other2):
    # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_C
        COUNTER_CLOCKWISE = 1   #左に曲がる場合(1)
        CLOCKWISE = -1          #右に曲がる場合(2)
        ONLINE_BACK = 2         #c<-a->b 反対に戻る(3)
        ONLINE_FRONT = -2       #a->b->c 同じ方向に伸びる(4)
        ON_SEGMENT = 0          #a->c->b 戻るがaとbの間(5)
    ###################################################################
        a, b, c = self, other1, other2
        ba, ca = b - a, c - a
        det = b.det(c)
        if det > EPS: return COUNTER_CLOCKWISE
        if det < -EPS: return CLOCKWISE
        if ba.dot(ca) < -EPS: return ONLINE_BACK
        if (a - b).dot(c - b) < -EPS: return ONLINE_FRONT
        return ON_SEGMENT

    @property
    def value(self):
        return self.x, self.y


######################################################################
class Line:
    """基本は線分"""
    def __init__(self, p0: Point, p1: Point):
        self.p0, self.p1 = p0, p1
        self.vector = p1 - p0

    @property
    def mid_point(self):
    # 中点
        return self.p0 + self.vector * 0.5

    @property
    def midperpendicular(self):
    # 垂直二等分線
    # 中点から中点＋直交ベクトルまでの線分とする
        return Line(self.mid_point, self.mid_point + self.vector.orthogonal)

    def is_parallel(self, other):
    #https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_A
    # ２直線の平行判定
        return abs(self.vector.det(other.vector)) < EPS

    def is_orthogonal(self, other):
    #https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_A
    # ２直線の直交判定
        return abs(self.vector.dot(other.vector)) < EPS

    def project(self, p: Point):
    # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_A
    # 垂線の足
        dv = self.p0.dot3(self.p1, p)
        dd = self.p0.dist2(self.p1)
        return self.p0 + self.vector * (dv/dd)

    def dist_from_point_to_project(self, p: Point):
        # 垂線の長さ
        return p.dist2(self.project(p)) ** 0.5

    def dist_from_point(self, p: Point):
        # 線分としての点からの距離
        dv = self.p0.dot3(self.p1, p)
        dd = self.p0.dist2(self.p1)
        if 0 <= dv <= dd:
            return p.dist2(self.project(p)) ** 0.5
        else:
            return min(self.p0.dist(p), self.p1.dist(p))

    def reflect(self, p: Point):
    # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/1/CGL_1_B
    # 反射
        return p + (self.project(p) - p) * 2

    def is_intersect(self, other):
    # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_B
    # 線分同士の交点判定
        p0, p1 = self.p0, self.p1
        q0, q1 = other.p0, other.p1
        C0, C1 = p0.det3(p1, q0), p0.det3(p1, q1)
        D0, D1 = q0.det3(q1, p0), q0.det3(q1, p1)
        if abs(C0) < EPS and abs(C1) < EPS:
            E0, E1 = p0.dot3(p1, q0), p0.dot3(p1, q1)
            if not E1 - E0 > 0:
                E0, E1 = E1, E0
            return p0.dist2(p1) - E0 > -EPS and E1 > -EPS
        return C0 * C1 < EPS and D0* D1 < EPS

    def cross_point(self, other):
    # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_C
    # 線分(直線含む)の交点
        if self.is_parallel(other): return None
        d = self.vector.det(other.vector)
        sn = (other.p0 - self.p0).det(other.vector)
        return self.p0 + self.vector * (sn/d)

    def dist_to_line(self, other):
    # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/2/CGL_2_D
    # 線分と線分の距離
        if self.is_intersect(other):
            return 0
        ret = float('inf')
        h = other.project(self.p0)
        if other.p0.counter_clockwise(other.p1, h) == 0:
            ret = min(ret, self.p0.dist(h))
        h = other.project(self.p1)
        if other.p0.counter_clockwise(other.p1, h) == 0:
            ret = min(ret, self.p1.dist(h))
        h = self.project(other.p0)
        if self.p0.counter_clockwise(self.p1, h) == 0:
            ret = min(ret, other.p0.dist(h))
        h = self.project(other.p1)
        if self.p0.counter_clockwise(self.p1, h) == 0:
            ret = min(ret, other.p1.dist(h))
        ret = min(ret, self.p0.dist(other.p0), self.p0.dist(other.p1))
        ret = min(ret, self.p1.dist(other.p0), self.p1.dist(other.p1))
        return ret

    def half_line(self, reverse=False):
    # 半直線
        d = self.vector.abs
        if reverse:
            return Line(self.p0, self.p0 + self.vector * MAX / d)
        return Line(self.p0 - self.vector * MAX / d, self.p1)

    def line(self):
    # 直線
        d = self.vector.abs
        return Line(self.p0 - self.vector * MAX / d, self.p0 + self.vector * MAX / d)

    @property
    def value(self):
        return self.p0.value, self.p1.value, self.vector

    def contains(self, p: Point):
        return self.p0.counter_clockwise(self.p1, p) == 0


######################################################################

x, y, u, v = map(int, input().split())
l1 = Line(Point(x, y), Point(u, v))
x, y, u, v = map(int, input().split())
l2 = Line(Point(x, y), Point(u, v))

if l1.is_intersect(l2):
    print('Yes')
else:
    print('No')