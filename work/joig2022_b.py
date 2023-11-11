# https://atcoder.jp/contests/joig2022-open/tasks/joig2022_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
a = list(map(int, input().split()))
ret = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if a[i] * a[j] == a[k]: ret+=1
print(ret)