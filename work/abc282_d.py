# https://atcoder.jp/contests/abc282/tasks/abc282_d

import sys
sys.setrecursionlimit(10**9)


def dfs(g,v,c):
    global color
    global b
    global w
    global e
    if c==1:
        b += 1
    elif c==-1:
        w += 1
    e += len(g[v])
    color[v] = c
    for nv in g[v]: # 次のノードの探索
        # すでに隣接の色が確定していて同じ色となっている場合終了
        if color[nv] == c: return False
        # 未確定の倍は反転させた色を塗って探索した結果を受け取る
        if color[nv] == 0 and not dfs(g,nv, -c): return False
    return True

#######################################

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

# 隣接リストの作成
for i in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    graph[a].append(b)
    graph[b].append(a)


color = [0] * n
ret = 0
ret2 = 0

for i in range(n):
    if color[i] != 0: continue
    b, w, e = 0, 0, 0
    ans = dfs(graph, i, 1)
    if not ans:
        print(0)
        exit()
    ret += b*w-e//2
    ret2 += (n- (b+w)) * (b+w)

print(ret+ret2//2)
