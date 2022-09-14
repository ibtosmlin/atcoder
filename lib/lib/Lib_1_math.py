#name#
# Lib_math
#description#
# mathのライブラリ
#body#
import math
print(math.sin(math.pi/4))
print(math.cos(math.pi/4))
print(math.tan(math.pi/4))
# 度→radian
math.radians(180)
# radian→度
math.degrees(3.1415)

print(math.gcd(x, y))
def lcm(x, y): return x * y // math.gcd(x, y)

#prefix#
# Lib_最大公約数_三角関数
# import math
#end#

#name#
# Lib_decimal
#description#
# 四捨五入が正しくできるツール
# Decimal で扱う
#body#
from decimal import Decimal
x, y, r = map(Decimal, input().split())
f = 123.456
fd = Decimal(str(f))
fr = fd.quantize(Decimal('0'), rounding=ROUND_HALF_UP)  #123
fr = fd.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)#123.5
#prefix#
# Lib_四捨五入_Decimal
#end#

#name#
# Lib_再帰関数
#description#
# 再帰関数
#body#
@lru_cache(maxsize=None)
#prefix#
# Lib_再帰関数
#end#

#name#
# Lib_複素数
#description#
# Lib_複素数
#body#
import cmath

z1 = 5 + 13j
a, b = 5, 13
z2 = complex(a, b)

print(z1.real)
print(z1.img)


# 極座標表示
r, theta = cmath.polar(z1)

print(cmath.rect(1, cmath.pi/2))
# (6.123233995736766e-17+1j)
print(z2.conjugate())
# (5-13j)

#prefix#
# Lib_再帰関数
#end#
