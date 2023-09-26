# https://atcoder.jp/contests/abc321/tasks/abc321_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

k = int(input())

ret = set(range(1, 10))
dp = set(range(1, 10))

for i in range(11):
    ndp = set()
    for x in dp:
        last = x % 10
        for i in range(last):
            ndp.add(x * 10 +i)
    ret |= ndp
    dp = ndp

print(sorted(ret)[k-1])

