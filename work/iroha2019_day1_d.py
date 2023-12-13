# https://atcoder.jp/contests/iroha2019-day1/tasks/iroha2019_day1_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
N, X, Y = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
u = X-Y+sum(A[0::2])-sum(A[1::2])
if u>0:
    print('Takahashi')
elif u == 0:
    print('Draw')
else:
    print('Aoki')
