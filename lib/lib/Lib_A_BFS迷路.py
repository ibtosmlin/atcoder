#name#
# 幅優先探索迷路
#description#
# 幅優先探索迷路
#body#
# 幅優先探索迷路
# 二次元マップ

from collections import deque

def bfs(g:list, st, gl=None) -> list:
    # 行く先設定
#    direc = {(1, 0), (-1, 0), (0, 1), (0, -1)}
    direc = {(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1) (-1, 1), (-1, -1)}

    # 幅優先探索
    h, w = len(g), len(g[0])
    seen = [[False] * w for _ in range(h)]
    level = [[-1] * w for _ in range(h)]    # 階層
    parent = [[-1] * w for _ in range(h)]   # 親node
    dp = [[-1] * w for _ in range(h)]       # dp 適宜設定
    # スタートの設定
    q = deque()
    u, v = st
    q.append(st)
    seen[u][v] = True
    level[u][v] = 0
    dp[u][v] = 0

    while q:
        cur = q.popleft()
        ch, cw = cur
        lvl = level[ch][cw]
        for dh, dw in direc:
            nh, nw = ch + dh, cw + dw
            nxt = (nh, nw)
            nlvl = lvl + 1
            if not (0<=nh<h and 0<=nw<w): continue
            if g[nh][nw]=='#':continue
            if seen[nh][nw]: continue
            q.append(nxt)
            seen[nh][nw] = True
            level[nh][nw] = nlvl
            parent[nh][nw] = (ch, cw)
            # dp[nh][nw] = .........
            if nxt == gl: return dp
    return dp


def find_start_goal(gmap):
    sstr = 's'; gstr = 'g'
    for h, gh in enumerate(gmap):
        if sstr in gh: start = (h, gh.index(sstr))
        if gstr in gh: goal = (h, gh.index(gstr))
    return start, goal


h, w = map(int,input().split())
gmap = [list(input()) for _ in range(h)]
st = (0, 0)
gl = (h-1, w-1)
# st, gl = find_start_goal(gmap)

ret = bfs(gmap, st, gl)

#prefix#
# lib_幅優先探索_迷路_BFS
#end#
