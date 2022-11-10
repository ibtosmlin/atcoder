# https://atcoder.jp/contests/abc276/tasks/abc276_b
n, m = map(int, input().split())
G = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    G[a-1].append(b)
    G[b-1].append(a)
for gi in G:
    gi.sort()
    print(len(gi), *gi)
