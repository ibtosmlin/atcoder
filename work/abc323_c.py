# https://atcoder.jp/contests/abc323/tasks/abc323_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, m = map(int, input().split())
A = list(map(int, input().split()))

p = []
mxp = -1
for i in range(n):
    s = input()
    po = i + 1
    no = []
    for i, si in enumerate(s):
        if si == 'o':
            po += A[i]
        else:
            no.append(A[i])
    no.sort(reverse=True)
    for i in range(1, len(no)):
        no[i] += no[i-1]
    p.append([po, no])
    mxp = max(mxp, po)

for i, (po, no) in enumerate(p):
    if po == mxp:
        print(0)
        continue
    t = 0
    while no[t] + po <= mxp:
        t += 1
    print(t+1)
