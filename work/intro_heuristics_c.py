# https://atcoder.jp/contests/intro-heuristics/tasks/intro_heuristics_c
connum = 26
d = int(input())
c = list(map(int, input().split()))
s = [list(map(int, input().split())) for _ in range(d)]

t = [int(input()) -1 for _ in range(d)]

def calc_score(t):
    sp_get = 0 # satisfy_point, unsatisfy_point
    sp_lost = 0
    last = [-1] * connum
    for di, ti in enumerate(t):
        last[ti] = di
        sp_get += s[di][ti]
        sp_lost += sum((c[tj] * (di - last[tj]) for tj in range(connum)))
        sp = sp_get - sp_lost
        # print(sp)
    return sp

score = calc_score(t)
m = int(input())
for _ in range(m):
    di, qi = map(lambda x: int(x)-1, input().split())
    t[di] = qi
    print(calc_score(t))