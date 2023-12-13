# https://atcoder.jp/contests/past15-open/tasks/past202306_j
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
N, M = map(int, input().split())

ret = 0
attack = []
for _ in range(N):
    a, b, x = map(int, input().split())
    if x == 0:
        ret += a*(b-1)
        attack.append((a, b-1))
    else:
        ret += a*b
        if b == 1:
            attack.append((a, 1))
        else:
            attack.append((2*a, 1))
            attack.append((a, b - 2))

attack.sort(reverse=True)

for a, b in attack:
    usem = min(M, b)
    M -= usem
    ret -= a * usem
    if M == 0: break

print(ret)
