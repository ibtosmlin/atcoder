# https://atcoder.jp/contests/abc333/tasks/abc333_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
port = [[] for _ in range(n)]
get = []
dp = [0] * (n+10)

for i in range(n):
    t, x = map(int, input().split())
    x -= 1
    if t == 1:
        port[x].append(i)
        get.append(i)
    else:
        if len(port[x]) == 0: exit(print(-1))
        j = port[x].pop()
        dp[j] += 1
        dp[i] -= 1

rdp = [0] * (n+10)
for i in range(n):
    rdp[i+1] = rdp[i] + dp[i]

print(max(rdp))
ret = []
for gi in get:
    if dp[gi]:
        ret.append(1)
    else:
        ret.append(0)
print(*ret)