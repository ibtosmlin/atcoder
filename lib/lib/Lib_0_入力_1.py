#name#
# n=intinput
#description#
# 整数nの読み込み
#body#
n = int(input())
a = list(map(int, input().split()))
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
G = [[] for _ in range($n)]
for _ in range($m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    G[a].append(b)
    G[b].append(a)

#prefix#
# G =
#end#

#name#
# edgesweighted
#description#
# edges(重み付き)
#body#
G = [[] for _ in range($n)]
for _ in range($m):
    a, b, w = map(int, input().split())
    a -= 1; b -= 1
    G[a].append((b, w))
    G[b].append((a, w))

#prefix#
# G = w
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
