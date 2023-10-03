# https://atcoder.jp/contests/cpsco2019-s4/tasks/cpsco2019_s4_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, k = map(int, input().split())
A = list(map(int, input().split())) + [10**10]
B = []
prev = A[0]
cnt = 0
for ai in A:
    if prev == ai:
        cnt += 1
    else:
        B.append(cnt)
        cnt = 1
        prev = ai

def isok(d):
    cnt = 0
    for bi in B:
        cnt += bi // (d+1)
    return cnt <= k

ok = n
ng = 0
while ok - ng > 1:
    mid = (ok+ng) // 2
    if isok(mid):
        ok = mid
    else:
        ng = mid
print(ok)