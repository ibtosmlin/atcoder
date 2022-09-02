#name#
# Lib_G_枝刈り取る
#description#
# グラフの葉から枝を刈り取って、ループ部分のみ抽出する
#body#
n = int(input())
edges = [[] for _ in range(n)]
degree = [0] * n
for _ in range(n):
    _a, _b = map(int1, input().split())
    edges[_a].append(_b)
    edges[_b].append(_a)
    degree[_a] += 1
    degree[_b] += 1

leaves = [i for i in range(n) if degree[i] == 1]
oncycle = set(range(n))
while leaves:
    x = leaves.pop()
    oncycle.remove(x)
    for y in edges[x]:
        degree[y] -= 1
        if degree[y] == 1:
            leaves.append(y)
#prefix#
# Lib_G_cycle
#end#
