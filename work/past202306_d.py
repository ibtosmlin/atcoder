# https://atcoder.jp/contests/past15-open/tasks/past202306_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
A, B, C, D, R = map(int, input().split())
rec = [0] * 2010
rec[A] += 1
rec[A+R] -= 1

t = ((B+(D-1))// D) * D
if t < C+R:
    rec[max(t, C)] += 1
    rec[C+R] -= 1

for i in range(2000):
    rec[i+1] += rec[i]

for i in range(C, C+R):
    if rec[i] == 0:
        print('No')
        exit()
print('Yes')
