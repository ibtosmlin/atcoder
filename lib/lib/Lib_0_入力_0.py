#name#
# intinput
#description#
# int型でのinput
#body#
int(input())
#prefix#
# intinput
#end#

#name#
# inputsplit
#description#
# inputをsplit
#body#
input().split()
#prefix#
# inputsplit
#end#

#name#
# mapint
#description#
# int型で複数数値のinput
#body#
map(int, input().split())
#prefix#
# mapintinput
#end#

#name#
# listmapint
#description#
# int型でlistのinput
#body#
list(map(int, input().split()))
#prefix#
# listmapintinput
#end#

#name#
# tuplemapint
#description#
# int型でtupleのinput
#body#
tuple(map(int, input().split()))
#prefix#
# tuplemapintinput
#end#

#name#
# matrixintinput
#description#
# int型でmatrixのinput
#body#
ma = [list(map(int, input().split())) for _ in range($n)]
#prefix#
# [listmapint
#end#

#name#
# matrixinput
#description#
# 文字列でmatrixのinput
#body#
ma = [list(input()) for _ in range($n)]
#prefix#
# [listinput()
#end#

#name#
# 転置行列
#description#
# 転置行列
#body#
tA = [list(x) for x in zip(*A)]
#prefix#
# transpose_matrix
#end#
