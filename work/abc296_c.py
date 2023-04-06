# https://atcoder.jp/contests/abc296/tasks/abc296_c
n, x = map(int, input().split())
a = frozenset(map(int, input().split()))
ax = frozenset([x+ai for ai in a])
if a & ax:
    print('Yes')
else:
    print('No')
