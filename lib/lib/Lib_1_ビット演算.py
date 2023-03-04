#name#
#description#
#body#
# BIT演算
#body#
# https://qiita.com/qiita_kuru/items/3a6ab432ffb6ae506758
# k桁目 or bitを0にする
x &= ~(1 << k)
x &= ~bit

# k桁目 or bitを1にする
x |= 1 << k
x |= bit

# k桁目 or bitを反転する
x ^= 1 << k
x ^= bit

# 111
~((~0)<<3)      # 111
(1 << 3) - 1    # 111

#prefix#
# Lib_BIT演算全部分集合
#end#



# BIT演算subset
#description#
# 集合Mの部分集合
#body#
# 集合Mの部分集合を列挙
def subset(n)->list:
    v = (-1) & n
    ret = []
    while v:
        ret.append(v)
        v = (v - 1) & n
    return ret
n = int('101', 2)
print(list(map(bin, subset(n))))
# ['0b101', '0b100', '0b1']

# サイズKの部分集合を列挙
def ksubset(n, k)->list:
    ret = []
    v = (1 << k) - 1
    while v < (1 << n):
        ret.append(v)
        x = v & -v; y = v + x
        v = ((v & ~y) // x >> 1) | y
    return ret
n, k = 5, 2
print(list(map(bin, ksubset(n, k))))
# ['0b11', '0b101', '0b110', '0b1001', '0b1010', '0b1100', '0b10001', '0b10010', '0b10100', '0b11000']

#prefix#
# Lib_BIT演算全部分集合
#end#
