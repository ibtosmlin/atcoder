# https://atcoder.jp/contests/abc342/tasks/abc342_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1


n = int(input())
s = input()

u = [chr(i+ord('a')) for i in range(26)]

q = int(input())
for _ in range(q):
    a, b = input().split()
    for j in range(26):
        if u[j] == a: u[j] = b

ret = []
for si in s:
    i = ord(si) - ord('a')
    ret.append(u[i])
print(''.join(ret))