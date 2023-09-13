# https://atcoder.jp/contests/abc319/tasks/abc319_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
ret = []
for i in range(n+1):
    x = False
    for j in range(1, 10):
        if n % j == 0:
            if i % (n // j) == 0:
                ret.append(str(j))
                x = True
                break
    if not x:
        ret.append(str('-'))

print(''.join(ret))