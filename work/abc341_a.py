# https://atcoder.jp/contests/abc341/tasks/abc341_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
n = int(input())
ret = [(i+1)%2 for i in range(2*n+1)]
print(''.join(map(str, ret)))