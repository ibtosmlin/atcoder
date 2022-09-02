#name#
# n=intinput
#description#
# 整数nの読み込み
#body#
n = int(input())
#prefix#
# n =int(input())
#end#

#name#
# s=input
#description#
# 文字列sの読み込み
#body#
s = list(input())
#prefix#
# s =list(input())
#end#

#name#
# ab=mapintinput
#description#
# 整数a, bの読み込み
#body#
a, b = map(int, input().split())
#prefix#
# a, b=map
#end#

#name#
# n,m=map(int, input().split())
#description#
# 整数n, mの読み込み
#body#
n, m = map(int, input().split())
#prefix#
# n, m=map
#end#

#name#
# n,k=map(int, input().split())
#description#
# 整数n, kの読み込み
#body#
n, k = map(int, input().split())
#prefix#
# n, k=map
#end#

#name#
# a=list(map(int, input().split()))
#description#
# リストの読み込み
#body#
a = list(map(int, input().split()))
#prefix#
# a =list
#end#

#name#
# b=list(map(int, input().split()))
#description#
# リストの読み込み
#body#
b = list(map(int, input().split()))
#prefix#
# b =list
#end#

#name#
# edges
#description#
# edges
#body#
edges = [[] for _ in range($n)]
for _ in range($m):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)

#prefix#
# edges =
#end#

#name#
# edgesweighted
#description#
# edges(重み付き)
#body#
edges = [[] for _ in range($n)]
for _ in range($m):
    _a, _b, _w = map(int, input().split())
    _a -= 1; _b -= 1
    edges[_a].append((_b, _w))
    edges[_b].append((_a, _w))

#prefix#
# edges = w
#end#

#name#
# 0インデックス
#description#
# 0-indexed
#body#
a -= 1; b -= 1
#prefix#
# a -= 1; b -= 1
#end#
