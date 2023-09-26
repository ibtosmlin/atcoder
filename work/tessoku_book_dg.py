# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_dg
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n,x,y = map(int, input().split())
A = list(map(int, input().split()))

def grundy(x):
    x = x % 5
    return [0,0,1,1,2][x]

xor = 0
for ai in A:
    xor ^= grundy(ai)
if xor:
    print('First')
else:
    print('Second')
