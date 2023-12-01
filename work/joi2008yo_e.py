# https://atcoder.jp/contests/joi2008yo/tasks/joi2008yo_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1


def popcount64(n):
    c=(n&0x5555555555555555)+((n>>1)&0x5555555555555555)
    c=(c&0x3333333333333333)+((c>>2)&0x3333333333333333)
    c=(c&0x0f0f0f0f0f0f0f0f)+((c>>4)&0x0f0f0f0f0f0f0f0f)
    c=(c&0x00ff00ff00ff00ff)+((c>>8)&0x00ff00ff00ff00ff)
    c=(c&0x0000ffff0000ffff)+((c>>16)&0x0000ffff0000ffff)
    c=(c&0x00000000ffffffff)+((c>>32)&0x00000000ffffffff)
    return c



R, C = map(int, input().split())
A = [0] * C

for i in range(R):
    ai = list(map(int, input().split()))
    for j in range(C):
        A[j] <<= 1
        A[j] += 1 - ai[j]

N = 1<<R
ret = 0
for s in range(N):
    now = 0
    for ai in A:
        u = popcount64(ai ^ s)
        now += max(R-u, u)
    ret = max(ret, now)
print(ret)