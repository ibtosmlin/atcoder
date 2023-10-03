# https://atcoder.jp/contests/dwacon2018-prelims/tasks/dwacon2018_prelims_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

s = list(map(int, list(input().replace('5', '1').replace('2', '0'))))
n = len(s)
if n%2 or sum(s) * 2 != n: exit(print(-1))

ret = 0
cnt = 0
for si in s:
    if si == 0:
        cnt += 1
        ret = max(ret, cnt)
    else:
        cnt -= 1
        if cnt < 0:
            exit(print(-1))
print(ret)