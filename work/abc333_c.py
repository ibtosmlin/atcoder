# https://atcoder.jp/contests/abc333/tasks/abc333_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
core = [1]
for i in range(120):
    core.append(core[-1] * 10 + 1)

nums = set()
for i in core:
    for j in core:
        for k in core:
            nums.add(i+j+k)
print(sorted(nums)[n-1])