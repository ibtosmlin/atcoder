# https://atcoder.jp/contests/abc339/tasks/abc339_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
C = dict()

n = int(input())
for _ in range(n):
    x = int(input())
    if not x in C:
        C[x] = 0
    C[x] += 1

A = sorted(C.keys())
m = len(A)
ret = 0
pat = set()
for k in range(m)[::-1]:
    Ak = A[k]
    for j in range(k+1):
        Aj = A[j]
        if Ak%Aj > 0: continue
        Ai = Ak // Aj
        if not Ai in C: continue
        if Ai > Aj:
            Ai, Aj = Aj, Ai
        pat.add((Ai, Aj, Ak))
for ai, aj, ak in pat:
    if ai == aj:
        if aj == ak:
            ret += C[ai] * (C[ai]-1) * (C[ai]-2)
        else:
            ret += C[ai] * (C[ai]-1) * C[ak]
    else:
        if aj == ak:
            ret += C[ai] * C[aj] * (C[aj]-1) * 2
        else:
            ret += C[ai] * C[aj] * C[ak] * 2
    print(ret, (ai, aj, ak))
print(ret)
