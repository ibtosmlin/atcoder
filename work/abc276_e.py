# https://atcoder.jp/contests/abc276/tasks/abc276_e
from collections import defaultdict, Counter, deque
def end(r=-1): print(r); exit()
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]# + [(1, 1), (1, -1), (-1, 1), (-1, -1)]
def isinhw(i, j, h, w): return (0 <= i < h) and (0 <= j < w)
h, w = map(int, input().split())
c = [input() for _ in range(h)]

for i in range(h):
    for j in range(w):
        if c[i][j] == 'S':
            sh = i
            sw = j
            break

def bfs(i, j):
    if not isinhw(i, j, h, w): return False
    if c[i][j] != '.': return False
    seen = [[-1] * w for _ in range(h)]
    que = deque([(i, j)])
    seen[i][j] = 1
    while que:
        ch, cw = que.popleft()
        for dh, dw in direc:
            nh = ch + dh
            nw = cw + dw
            nv = seen[ch][cw] + 1
            if not isinhw(nh, nw ,h, w): continue
            if c[nh][nw] == '#': continue
            if c[nh][nw] == 'S':
                if nv < 4: continue
                else: return True
            if seen[nh][nw] != -1: continue
            seen[nh][nw] = nv
            que.append((nh, nw))
#    print(i, j, seen)
    return False

for dh, dw in direc:
    if bfs(sh+dh, sw+dw):
        end('Yes')

end('No')
