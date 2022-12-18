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
[list(map(int, input().split())) for _ in range($n)
#prefix#
# [listmapint
#end#

#name#
# matrixinput
#description#
# 文字列でmatrixのinput
#body#
[list(input()) for _ in range($n)
#prefix#
# [listinput()
#end#

#name#
# matrixinput
#description#
# 文字列でmatrixのinput
#body#
[tuple(map(int, input().split())) for _ in range($n)
#prefix#
# [tupleinput()
#end#
