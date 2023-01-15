#name#
# Lib_図形
#description#
# 図形のライブラリ
#body#

import cmath
import math

# 円の交差判定
########################

def dist2(pt1, pt2): return sum([(x1-x2) ** 2 for x1, x2 in zip(pt1, pt2)])
def distPtoP(pt1, pt2): return dist2(pt1, pt2) ** 0.5
def distCtoC(c1, c2):
    pt1, r1 = c1; pt2, r2 = c2; R, r, d = max(r1, r2), min(r1, r2), distPtoP(pt1, pt2)
    return d-R-r if d > R+r else R-r-d if d < R-r else 0
    # d > R+r :O o
    # d < R-r: ◎
    # else 交差
########################

# 反時計回りかどうか/内角が180以上/凸
########################
def ccw(p1, p2, p3):
    x1, y1 = p1[0] - p2[0], p1[1] - p2[1]
    x3, y3 = p3[0] - p2[0], p3[1] - p2[1]
    return x1 * y3 - x3 * y1 > 0
########################


# 円の交差判定
########################
import math

# 度→radian
math.radians(180)
# radian→度
math.degrees(3.1415)
########################


# 二辺とそれを挟む角度
########################
# 余弦定理
# cosR = (a**2 + b**2 - c**2) / 2ab
# c**2 = a**2 + b**2 - 2*a*b*cosR
# 対辺
def C(a, b, R):
    return (a ** 2 + b** 2 - 2*a*b*math.cos(R))**0.5
# 面積
def S(a, b, R):
    return abs(0.5 * a * b * math.sin(R))
########################



#prefix#
# Lib_図形
#end#
