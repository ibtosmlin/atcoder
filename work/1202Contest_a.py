# https://atcoder.jp/contests/DEGwer2023/tasks/1202Contest_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
N, K, T = map(int, input().split())
A = sorted(map(int, input().split()))
pv = -1
ret = 0
for nw in A:
    if pv > 0 and pv+T > nw:
        ret += 1
    else:
        pv = nw
print(ret)
