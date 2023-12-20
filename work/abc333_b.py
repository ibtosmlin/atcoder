# https://atcoder.jp/contests/abc333/tasks/abc333_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
u = 'ABCDE'
ab = sorted(list(input()))
cd = sorted(list(input()))

ab = u.index(ab[1]) - u.index(ab[0])
if ab > 2: ab = 5-ab

cd = u.index(cd[1]) - u.index(cd[0])
if cd > 2: cd = 5-cd

print('Yes' if ab==cd else 'No')