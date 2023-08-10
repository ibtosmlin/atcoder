# https://atcoder.jp/contests/abc313/tasks/abc313_a
n = int(input())
a = list(map(int, input().split()))
a[0] -= 1
print(max(a)-a[0])