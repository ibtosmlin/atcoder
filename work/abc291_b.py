# https://atcoder.jp/contests/abc291/tasks/abc291_b
n = int(input())
x = list(map(int, input().split()))
x.sort()
y = x[n:4*n]
#print(y)
print(sum(y) / 3 / n)