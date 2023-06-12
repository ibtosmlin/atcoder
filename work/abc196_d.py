# https://atcoder.jp/contests/abc196/tasks/abc196_d
H, W, A, B = map(int, input().split())
ret = 0

def dfs(i, j, p, np, a, b):
    # print(i, j, p, np, a, b)
    global ret
    if i == H and j == 0:
        ret += 1
        return
    if p[j]:
        if j+1 < W:
            dfs(i, j+1, p, np, a, b)
        else:
            dfs(i+1, 0, np, [False] * W, a, b)
    else:
        if b >= 1:
            _p = p[:]
            _p[j] = True
            if j+1 < W:
                dfs(i, j+1, _p, np, a, b-1)
            else:
                dfs(i+1, 0, np, [False] * W, a, b-1)
        if a >= 1:
            _p = p[:]
            _p[j] = True
            _np = np[:]
            _np[j] = True
            if j+1 < W:
                dfs(i, j+1, _p, _np, a-1, b)
            else:
                dfs(i+1, 0, _np, [False] * W, a-1, b)
        if a >= 1 and j+1 < W and not p[j+1]:
            _p = p[:]
            _p[j] = True
            _p[j+1] = True
            if j+2 < W:
                dfs(i, j+2, _p, np, a-1, b)
            else:
                dfs(i+1, 0, np, [False] * W, a-1, b)
        return


dfs(0,0,[False]*W,[False]*W,A,B)
print(ret)