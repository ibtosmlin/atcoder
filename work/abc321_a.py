# https://atcoder.jp/contests/abc321/tasks/abc321_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = input()

for i in range(len(n)-1):
    if n[i] > n[i+1]: continue
    print('No')
    exit()

print('Yes')
exit()


