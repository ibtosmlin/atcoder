# https://atcoder.jp/contests/iroha2019-day2/tasks/iroha2019_day2_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
H = [int(input()) for _ in range(n)]
d = {u: i+1 for i, u in enumerate(sorted(set(H)))}
for hi in H:
    print(d[hi])
