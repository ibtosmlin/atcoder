# https://atcoder.jp/contests/bitflyer2018-final/tasks/bitflyer2018_final_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
ret = 101
for _ in range(n):
    p = int(input())
    cnt = 0
    while p%10==0:
        p //= 10
        cnt += 1
    ret = min(ret, cnt)
print(ret)