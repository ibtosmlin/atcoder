# https://atcoder.jp/contests/abc328/tasks/abc328_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
D = list(map(int, input().split()))
ret = 0
for i in range(1, n+1):
    for j in range(1, D[i-1]+1):
        u = str(i) + str(j)
        if len(set(list(u))) == 1:
            ret += 1
print(ret)