#name#
# lib_math
#description#
# mathのライブラリ
#body#
import math
print(math.sin(math.pi/4))
print(math.cos(math.pi/4))
print(math.tan(math.pi/4))
print(math.gcd(x, y))
#prefix#
# lib_最大公約数_三角関数
# import math
#end#

#name#
# lib_decimal
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
# lib_四捨五入_Decimal
#end#

#name#
# lib_再帰関数
#description#
# 再帰関数
#body#
@lru_cache(maxsize=None)
#prefix#
# lib_再帰関数
#end#
