# https://atcoder.jp/contests/newjudge-2308-algorithm/tasks/abc244_c
n = int(input())
n = 2*n+1
seen = [False] * (n+1)
now = 1
while now <= n:
    if not seen[now]:
        print(now, flush=True)
        seen[now] = True
        seen[int(input())] = True
    now += 1
