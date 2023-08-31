# https://atcoder.jp/contests/arc108/tasks/arc108_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1: lambda x: int(x) - 1

mod = 1000000007
n = int(input())
aa = input()
ab = input()
ba = input()
bb = input()

if ab == "B":
    if aa == "A":
        aa = "B"
    else:
        aa = "A"
    if ba == "A":
        ba = "B"
    else:
        ba = "A"
    if bb == "A":
        b = "B"
    else:
        bb = "A"

if aa == 'A':
    exit(print(1))
if ba == 'A':
    exit(print(pow(2, n-2, mod)))
if 
