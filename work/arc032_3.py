# https://atcoder.jp/contests/arc032/tasks/arc032_3
n = int(input())
lrs = []
for i in range(n):
    l, r = map(int, input().split())
    lrs.append((l, r+1, i))

dp = [[] *  for _ in range(n+1)]