# https://atcoder.jp/contests/abc334/tasks/abc334_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

a, m, l, r = map(int, input().split())

def c(x):
    d = abs(x-a)
    return d // m + 1

if l < a < r:
    ret = c(r) + c(l) - 1
    print(ret)
    exit()
if l == a:
    ret = c(r)
    print(ret)
    exit()
if r == a:
    ret = c(l)
    print(ret)
    exit()

if a < l:
    ret = c(r) - c(l-1)
    print(ret)
    exit()

ret = c(l) - c(r+1)
print(ret)
exit()
