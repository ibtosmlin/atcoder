# https://atcoder.jp/contests/aising2019/tasks/aising2019_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

from bisect import bisect_right, bisect_left
n, q = map(int, input().split())
A = sorted(map(int, input().split()))
RA0 = [0]
RA1 = [0]
for i, ai in enumerate(A):
    if i%2:
        RA1.append(RA1[-1] + ai)
        RA0.append(RA0[-1])
    else:
        RA0.append(RA0[-1] + ai)
        RA1.append(RA1[-1])
RA0 = RA0[1:]
RA1 = RA1[1:]

print(A)
print(RA0)
print(RA1)

for _ in range(q):
    x = int(input())
    l = bisect_right(A, x)
    r = n - 1
    if l >= r - 1:
        if n%2:
            print(RA0[-1])
        else:
            print(RA1[-1])
        continue
    print(x, l, r)