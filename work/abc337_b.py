# https://atcoder.jp/contests/abc337/tasks/abc337_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

s = input()
for i in range(101):
    for j in range(101):
        for k in range(101):
            u = 'A' * i + 'B' * j + 'C' * k
            if u == s:
                exit(print('Yes'))
print('No')
