# https://atcoder.jp/contests/joi2022yo2/tasks/joi2022_yo2_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

q = int(input())
stack = []
for _ in range(q):
    s = input()
    if s == 'READ':
        print(stack.pop())
    else:
        stack.append(s)
