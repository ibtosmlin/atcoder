#name#
# Lib_AL_図形_n角形/円
#description#
# 図形のライブラリ
#body#

import math
EPS = 1e-08
MAX = 2e09
PI = math.pi

######################################################################
class Point:
    def __init__(self, x, y):
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

    @property
    def abs(self):
        return (self.x **2 + self.y **2)**0.5

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

    @property
    def radian(self):
        return math.atan3(self.y, self.x)

    def rotate_radian(self, R):
        cos, sin = math.cos(R), math.sin(R)
        return Point(self.x * cos - self.y * sin, self.x * sin + self.y * cos)

    def rotate_degree(self, R):
        R = math.radians(R)  # Rが度数の場合
        return self.rotate_radian(R)

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

####################
# x, y = map(int, input().split())
# p = Point(x, y)
####################

######################################################################
class Line:
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
        orthogonal_vec = Point(self.vector.y, -self.vecotor.x)
        return Line(self.mid_point, self.mid_point + orthogonal_vec)

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

    def dist_from_point(self, p: Point):
        # 垂線の長さ
        return p.dist2(self.project(p)) ** 0.5

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
    # 直線の交点
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

####################
# x, y, u, v = map(int, input().split())
# l = Line(Point(x, y), Point(u, v))
####################

######################################################################

class Polygon:
    def __init__(self, pts: list):
        self.N = len(pts)
        self.points = [Point(x, y) for x, y in pts]
        self.pts = pts

    @property
    def value(self):
        return self.pts

    @property
    def area(self):
    # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/3/CGL_3_A
    # 多角形の面積
    # O(N)
        P = self.points
        return abs(sum(P[i].det(P[i-1]) for i in range(self.N))) / 2

    @property
    def is_convex(self):
    # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/3/CGL_3_B
    # 凸性判定
    # O(N)
        P = self.points
        return not any((P[i-2].counter_clockwise(P[i-1], P[i]) == -1 for i in range(self.N)))

    def contains(self, p:Point):
    # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/3/CGL_3_C
    # 多角形-点の包含 凸多角形とは限らない
    # O(N)
        """
        returns
        0: not
        1: on 線上
        2: contain 包含
        """
        ON_EDGE = 1
        INCLUDE = 2
        NOT_INCLUDE = 0
        included = False
        for i in range(self.N):
            p0, p1 = self.points[i-1] - p, self.points[i] - p
            if abs(p0.det(p1)) < EPS and p0.dot(p1) < EPS: return ON_EDGE
            if p0.y > p1.y: p0, p1 = p1, p0
            if p0.y < EPS < p1.y and p0.det(p1) > EPS: included = not included
        if included: return INCLUDE
        return NOT_INCLUDE

    @property
    def convex_hull(self):
        # https://onlinejudge.u-aizu.ac.jp/problems/CGL_4_A
        # ps = [(x, y), ...]
        # 凸包(点集合 P の全ての点を含む最小の凸多角形)を出力する
        # O(N)
        _pts = sorted(self.pts)
        qs = []
        N = len(_pts)
        for x, y in _pts:
            p = Point(x, y)
            while len(qs) > 1 and qs[-1].det3(qs[-2], p) > EPS:
                qs.pop()
            qs.append(p)
        t = len(qs)
        for i in range(N-1)[::-1]:
            x, y = _pts[i]
            p = Point(x, y)
            while len(qs) > t and qs[-1].det3(qs[-2], p) > EPS:
                qs.pop()
            qs.append(p)
        return Polygon([pi.value for pi in qs[:-1]])

    @property
    def diameter(self):
        # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/4/CGL_4_B
        # 凸多角形の直径
        # O(N)
        ch = self.convex_hull
        if ch.N == 2:
            return ch.points[0].dist(ch.points[1])
        i = j = 0
        for k in range(ch.N):
            if ch.points[k].value < ch.points[i].value: i = k
            if ch.points[j].value < ch.points[k].value: j = k
        ret = 0
        si = i; sj = j
        while i != sj or j != si:
            ret = max(ret, ch.points[i].dist(ch.points[j]))
            if (ch.points[i]-ch.points[i-ch.N+1]).det(ch.points[j]-ch.points[j-ch.N+1])  < -EPS:
                i = (i+1) % ch.N
            else:
                j = (j+1) % ch.N
        return ret

    def convex_cut(self, l: Line):
        # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/4/CGL_4_C
        # 凸多角形を直線で切った時の右側の多角形
        q = []
        for i in range(self.N):
            p0, p1 = self.points[i-1], self.points[i]
            cv0, cv1 = l.p0.det3(l.p1, p0), l.p0.det3(l.p1, p1)
            if cv0 * cv1 < EPS:
                v = l.cross_point(Line(p0, p1))
                if v is not None: q.append(v.value)
            if cv1 > -EPS: q.append(p1.value)
        return Polygon(q)

    def contains(self, p: Point):
        # https://atcoder.jp/contests/abc296/tasks/abc296_g
        # ある点が凸多角形に入っているか
        ON_EDGE = 1
        INCLUDE = 2
        NOT_INCLUDE = 0
        ######################
        left = 1; right = self.N
        q0 = self.points[0]
        while right - left > 1:
            mid = (left + right) // 2
            if q0.det3(p, self.points[mid]) < EPS: left = mid
            else: right = mid
        if left == self.N-1:
            left -= 1
        qi = self.points[left]; qj = self.points[left + 1]
        v0 = q0.det3(qi, qj)
        v1, v2 = q0.det3(p, qj), q0.det3(qi, p)
        if v0 < -EPS:
            v1 = -v1; v2 = -v2
        if 0 <= v1 and 0 <= v2 and v1 + v2 <= v0:
            if left == 1 and abs(v2) < EPS: return ON_EDGE
            if left + 1 == self.N - 1 and abs(v1) < EPS: return ON_EDGE
            if abs(v1 + v2 - v0) < EPS: return ON_EDGE
            return INCLUDE
        return NOT_INCLUDE

####################
# pol = Polygon([tuple(map(int, input().split())) for _ in range(n)])
####################

######################################################################

class Circle:
    def __init__(self, p: tuple, r: float):
        self.center = Point(p[0], p[1])
        self.radius = r

    @property
    def value(self):
        return self.center, self.radius

    @property
    def area(self):
        return PI * self.radius * self.radius

    def contain_point(self, p:Point):
        return (p - self.center).abs - self.radius < -EPS

    def is_intersect(self, other):
    # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_A
    # 円の交差判定
    # 接線の数を出力
        OUTER = 4           # 離れている
        CIRCUMSCRIBED = 3   # 外接
        CROSSED = 2           # 交わる
        INSCRIBED = 1       # 内接
        CONTAINED = 0         # 包含

        R = max(self.radius, other.radius)
        r = min(self.radius, other.radius)
        d = self.center.dist(other.center)
        # d > R+r :O o | d < R-r: ◎ | else 交差
        if d - R - r > EPS: return OUTER
        elif d - R - r > -EPS : return CIRCUMSCRIBED
        if R - r - d > EPS: return CONTAINED
        elif R - r -d > -EPS: return INSCRIBED
        return CROSSED

    def cross_point_line(self, l: Line, restrict=False):
        # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_D
        # 直線との交点
        # restrict == True なら線分として判定
        p0c = l.p0 - self.center
        a = l.vector.abs ** 2
        b = l.vector.dot(p0c)
        c = p0c.abs ** 2 - self.radius ** 2
        D = b**2 - a * c
        if D < -EPS: return (None, None)
        if D < EPS: D = 0
        s1 = (- b + D**0.5) / a
        p1 = l.p0 + l.vector * s1
        s2 = (- b - D**0.5) / a
        p2 = l.p0 + l.vector * s2
        if restrict:
            if not (0 <= s1 <= 1): p1 = None
            if not (0 <= s2 <= 1): p2 = None
        return (p1, p2)

    def cross_point_circle(self, other):
        # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_E
        # 円同士の交点
        d = other.center - self.center
        rr0 = d.abs ** 2
        rr1 = self.radius ** 2
        rr2 = other.radius ** 2
        cv = rr0 + rr1 - rr2
        sv = (4*rr0*rr1 - cv**2)**0.5
        p1 = Point(cv * d.x - sv * d.y, cv * d.y + sv * d.x) / (2 * rr0)
        p1 = self.center + p1
        p2 = Point(cv * d.x + sv * d.y, cv * d.y - sv * d.x) / (2 * rr0)
        p2 = self.center + p2
        return (p1, p2)

    def tangent_point(self, p:Point):
        # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_F
        # 円と点の接点
        if self.contain_point(p): return None
        r = ((self.center - p).abs ** 2 - self.radius ** 2) ** 0.5
        dummycircle = Circle(p.value, r)
        return self.cross_point_circle(dummycircle)

    def tangent_line(self, p:Point):
        # 円と点の接線
        return Line(p, self.tangent_point)

    def common_tanget_outer(self, other):
        # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_G
        # 円と円の共通接線の外接点
        retext = []
        d = other.center - self.center
        rr0 = d.abs ** 2
        cv  = self.radius - other.radius
        sv = rr0 - cv ** 2
        if sv > -EPS:
        ## 外接線
            if abs(sv) < EPS:
                retext.append(self.center + d * (self.radius * cv / rr0))
            else:
                sv **= 0.5
                retext.append(self.center + Point(cv*d.x - sv*d.y, sv*d.x + cv*d.y) * self.radius / rr0)
                retext.append(self.center + Point(cv*d.x + sv*d.y, -sv*d.x + cv*d.y) * self.radius / rr0)
        return retext


    def common_tanget_inner(self, other):
        # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_G
        # 円と円の共通接線の内接点
        retext = []
        d = other.center - self.center
        rr0 = d.abs ** 2
        cv  = self.radius + other.radius
        sv = rr0 - cv ** 2
        if sv > -EPS:
        ## 内接線
            if abs(sv) < EPS:
                retext.append(self.center + d * (self.radius * cv / rr0))
            else:
                sv **= 0.5
                retext.append(self.center + Point(cv*d.x - sv*d.y, sv*d.x + cv*d.y) * self.radius / rr0)
                retext.append(self.center + Point(cv*d.x + sv*d.y, -sv*d.x + cv*d.y) * self.radius / rr0)
        return retext


####################
# x, y, r = map(int, input().split())
# C0 = Circle((x, y), r)
####################

######################################################################

class Triangle(Polygon):
    def __init__(self, pts):
        assert len(pts) == 3, "Not 3 points"
        super().__init__(pts)

    @property
    def circle_in(self):
        # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_B
        # 内接円
        dp1 = self.points[1] - self.points[0]
        dp2 = self.points[2] - self.points[0]
        dd = [(self.points[2] - self.points[1]).abs, dp2.abs, dp1.abs]
        dsum = sum(dd)
        r = abs(dp1.det(dp2)) / dsum
        c = Point(0, 0)
        for ci, ddi in zip(self.points, dd):
            c = c + ci * ddi
        c = c / dsum
        return Circle(c.value, r)

    @property
    def circle_circumscribed(self):
        # https://onlinejudge.u-aizu.ac.jp/courses/library/4/CGL/7/CGL_7_C
        # 外接円
        dp1 = (self.points[0] - self.points[1]) * 2 # a, b
        dp2 = (self.points[0] - self.points[2]) * 2 # c, d
        p = self.points[0].abs ** 2 - self.points[1].abs ** 2
        q = self.points[0].abs ** 2 - self.points[2].abs ** 2
        det = dp1.det(dp2)
        x = dp2.y * p - dp1.y * q
        y = dp1.x * q - dp2.x * p
        if det < -EPS:
            x *= -1; y *= -1; det *= -1
        x /= det; y /= det
        r = Point(x, y).dist(self.points[0])
        return Circle((x, y), r)

####################
# T = Polygon([tuple(map(int, input().split())) for _ in range(3)])
####################

######################################################################


#prefix#
# Lib_AL_図形_n角形/円
#end#
