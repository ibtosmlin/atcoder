# https://atcoder.jp/contests/abc342/tasks/abc342_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n = int(input())
P = list(map(int1, input().split()))
Q = int(input())

R = {pi:i for i, pi in enumerate(P)}

for _ in range(Q):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    if R[a] < R[b]:
        print(a+1)
    else:
        print(b+1)
