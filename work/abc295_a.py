# https://atcoder.jp/contests/abc295/tasks/abc295_a
n = int(input())
W = set(input().split())
A = {'and', 'not', 'that', 'the', 'you'}
print('Yes' if W & A else 'No')
