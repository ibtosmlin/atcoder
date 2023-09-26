# https://atcoder.jp/contests/ttpc2019/tasks/ttpc2019_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, x = map(int, input().split())
A = list(map(int, input().split()))
xa = x
c = 0
cpos = []
for i, a in enumerate(A):
    if a == -1:
        c += 1
        cpos.append(i)
    else:
        xa ^= a

if c == 0 and xa == 0:
    print(*A)
    exit()

elif c==1 and xa <= x:
    A[cpos[0]] = xa
    print(*A)
    exit()

elif c >= 2:
    k = max([i for i in range(32) if xa >> i])
    u = 1<<k
    if u <= x:
        xa ^= u
        if xa <= x:
            A[cpos[0]] = xa
            A[cpos[1]] = u
            for i in cpos[2:]:
                A[i] = 0
            print(*A)
            exit()

print(-1)