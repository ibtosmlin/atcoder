# https://atcoder.jp/contests/pakencamp-2021-day2/tasks/pakencamp_2021_day2_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

IDSA = [False] * 3001
IDSB = [False] * 3001

for ai in a:
    IDSA[ai] = True
for bi in b:
    IDSB[bi] = True

ret = []
for i in range(3001):
    if IDSB[i] and (not IDSA[i]):
        ret.append(i)
print(len(ret))
print('\n'.join(map(str, ret)))