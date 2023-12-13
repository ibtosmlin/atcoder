# https://atcoder.jp/contests/past15-open/tasks/past202306_g
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n, m = map(int, input().split())

con = [[] for _ in range(m)]
for i in range(m):
    k = int(input())
    for _ in range(k):
        a, b = map(int, input().split())
        a -= 1
        con[i].append((a, b))

def isok(s):
    for i in range(m):
        f = False
        for a, b in con[i]:
            if s >> a & 1 == b:
                f = True
                break
        if f == False:
            return False
    return True

for s in range(1<<n):
    if isok(s):
        exit(print('Yes'))
exit(print('No'))
