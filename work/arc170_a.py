# https://atcoder.jp/contests/arc170/tasks/arc170_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n = int(input())
S = input()
T = input()

for si, ti in zip(S, T):
    if si == ti == "B": continue
    if si == "A" and ti == "B":
        exit(print(-1))
    if ti == "A": break

for si, ti in zip(S[::-1], T[::-1]):
    if si == ti == "A": continue
    if si == "B" and ti == "A":
        exit(print(-1))
    if ti == "B": break

ret = 0
bcnt = 0
for si, ti in zip(S, T):
    if si == ti: continue
    if si == "A" and ti == "B":
        if bcnt:
            bcnt -= 1
        else:
            ret += 1
    if si == "B" and ti == "A":
        ret += 1
        bcnt += 1
    # print(si, ti, ret, bcnt)
print(ret)