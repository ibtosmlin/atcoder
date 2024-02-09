# https://atcoder.jp/contests/oupc2023-day1/tasks/oupc2023_day1_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

N, M = map(int, input().split())


def conv(s):
    return "".join([chr((ord(si)-ord(s[0]))%26+ord('a')) for si in s])

d = dict()
for _ in range(N):
    s = input()
    d[conv(s)] = s

q = int(input())
while q:
    t = input()
    print(d[conv(t)])
    q -= 1