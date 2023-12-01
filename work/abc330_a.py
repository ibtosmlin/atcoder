# https://atcoder.jp/contests/abc330/tasks/abc330_a
n, l = map(int, input().split())
print(sum(1 for ai in map(int, input().split()) if ai >=l))
