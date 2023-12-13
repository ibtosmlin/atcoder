# https://atcoder.jp/contests/joi2007yo/tasks/joi2007yo_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
A, B, C = map(int, input().split())
N = A+B+C
q = int(input())
ret = [2] * (A+B+C+1)
res = [list(map(int, input().split())) for _ in range(q)]
for a, b, c, f in res:
    if f:
        ret[a] = ret[b] = ret[c] = 1

def check(a, b, c):
    global ret
    if ret[a] == 1 and ret[b] == 1:
        ret[c] = 0

for a, b, c, f in res:
    if not f:
        check(a, b, c)
        check(b, c, a)
        check(c, a, b)

for i in range(1, N+1):
    print(ret[i])
