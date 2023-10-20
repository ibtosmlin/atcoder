# https://atcoder.jp/contests/wtf22-day1-open/tasks/wtf22_day1_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, m, a, b = map(int, input().split())
cnt = [0] * n
for xi in list(map(int1, input().split())):
    cnt[xi] += 1

cnt.sort()

ret = 0
i = 0
while b - >= 0:
    ret += 1
    b -=
    i += 1