# https://atcoder.jp/contests/abc331/tasks/abc331_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n, s, m, l = map(int, input().split())
ret = 10**20
for i in range(n+1):
    for j in range(n+1):
        for k in range(n+1):
            cnt = 6 * i  + 8 * j + 12 * k
            mon = s * i  + m * j + l * k
            if cnt >= n:
                ret = min(ret, mon)
print(ret)