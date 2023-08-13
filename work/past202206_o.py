# 部分和の計算と要素の更新の両方を効率的に行える
# 1-indexed
# sum(r)        :閉区間 [0,r] の合計を取得する
# [8] a0 + a1  + a2 + a3 + a4 + a5 + a6 + a7
# [4] a0 + a1  + a2 + a3
# [2] a0 + a1               [6] a4 + a5
# [1] a0       [3] a2       [5] a4        [7] a6

#                   [1000]
#           [0100]
#   [0010]                [0110]
# [0001]    [0011]      [0111]      [1111]
class BinaryIndexedTree:
    # 初期化処理
    def __init__(self, size):
        self.size = size
        self.dat = [0]*(size+1)
        self.depth = size.bit_length()

    def init(self, a):
        for i, x in enumerate(a):
            self.add(i, x)

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.dat[i] += x
            i += i & -i # 更新すべき位置

    def update(self, i, x):
        x -= self[i]
        self.add(i, x)

    def sum(self, r):
        """
        Returns
        -------
        sum of [0, r]
        """
        r += 1
        ret = 0
        while r>0:
            ret += self.dat[r]
            r -= r & -r # 加算すべき位置
        return ret

    def range_sum(self, l, r):
        """閉区間 [l,r] の合計を取得する

        Returns
        -------
        sum of [l, r]
        """
        if l == 0:
            return self.sum(r)
        else:
            return self.sum(r) - self.sum(l-1)


    def __getitem__(self, i):
        return self.range_sum(i, i)


    def right_bound_of_x(self, x):
        # pos       : sum([0, pos]) < x     となる最大のindex
        sum_, pos = 0, 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.dat[k] <= x:
                sum_ += self.dat[k]
                pos += 1 << i
        return pos

    def right_bound_include_x(self, x):
        # pos       : sum([0, pos]) <= x     となる最大のindex
        sum_, pos = 0, 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.dat[k] < x:
                sum_ += self.dat[k]
                pos += 1 << i
        return pos

    def left_bound_of_x(self, x):
        # pos   : x < sum([0, pos])  となる最小のindex
        return self.right_bound_include_x(x) - 1

    def left_bound_include_x(self, x):
        # pos   : x <= sum([0, pos])  となる最小のindex
        return self.right_bound_of_x(x) - 1


#### for debug
    def _get_original_sequence(self):
        ret = [self[i] for i in range(self.size)]
        return ret

    def _get_aggrigate_sequence(self):
        return [self.sum(i) for i in range(self.size)]

    def __str__(self):
        seq = self._get_original_sequence()
        ret = 'original :' + ' '.join(map(str, seq))
        ret += '\n'
        seq = self._get_aggrigate_sequence()
        ret += 'aggrigate:' + ' '.join(map(str, seq))
        return ret

########################################


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

mod = 998244353
q = int(input())
point = []
query = []
for i in range(q):
    f, x, y = input().split()
    p = Point(int(x), int(y))
    _p = Point(-int(x), - int(y))
    point.append(p)
    point.append(_p)
    query.append((p, _p, f))

point = {p: i for i, p in enumerate(sorted(point))}


n = len(point)
bitx = BinaryIndexedTree(n)
bity = BinaryIndexedTree(n)
ret = 0
for p, _p, f in query:
    i = point[p]
    j = point[_p]
    now = 0
    if i < j:
        now += bitx.range_sum(0, i) * p.y - bity.range_sum(0, i) * p.x
        now -= bitx.range_sum(i, j) * p.y - bity.range_sum(i, j) * p.x
        now += bitx.range_sum(j, n-1) * p.y - bity.range_sum(j, n-1) * p.x
        now %= mod
    else:
        now -= bitx.range_sum(0, j) * p.y - bity.range_sum(0, j) * p.x
        now += bitx.range_sum(j, i) * p.y - bity.range_sum(j, i) * p.x
        now -= bitx.range_sum(i, n-1) * p.y - bity.range_sum(i, n-1) * p.x
        now %= mod
    if f == "+":
        ret += now
        bitx.add(i, p.x%mod)
        bity.add(i, p.y%mod)
    else:
        ret -= now
        bitx.add(i, -p.x%mod)
        bity.add(i, -p.y%mod)
    ret %= mod
    print(ret)
