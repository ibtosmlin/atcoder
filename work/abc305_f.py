# https://atcoder.jp/contests/abc305/tasks/abc305_f

n, m = map(int, input().split())

seen = [False] * (n+1)
parent = [-1] * (n+1)

def dfs(x):
    global seen
    s = input()
    if s == 'OK': exit()
    nxs = list(map(int, s.split()))[1:][::-1]
    for nx in nxs:
        if seen[nx]: continue
        seen[nx] = True
        parent[nx] = x
        print(nx, flush=True)
        dfs(nx)
    p = parent[x]
    print(p, flush=True)
    dfs(p)
    return

seen[1] = True
dfs(1)
