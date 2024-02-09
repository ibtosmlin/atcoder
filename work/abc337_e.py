# https://atcoder.jp/contests/abc337/tasks/abc337_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

N = int(input())
m = len(bin(N-1))-2

for i in range(m):
    l = []
    for j in range(N):
        if j >> i & 1:
            l.append(j+1)
    print(len(l), *l)

s = input()
ret = int(s[::-1], 2) + 1
print(ret)