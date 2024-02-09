# https://atcoder.jp/contests/abc337/tasks/abc337_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n = int(input())
a = list(map(int1, input().split()))
d = {}
for i in range(n):
    d[a[i]] = i

now = d[-2]
ret = [now]
for _ in range(n-1):
    ret.append(d[now])
    now = d[now]
ret = [x+1 for x in ret]
print(*ret)
