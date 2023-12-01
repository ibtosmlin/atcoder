# https://atcoder.jp/contests/abc329/tasks/abc329_e
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n, m = map(int, input().split())
s = list(input())
t = list(input())

def ok(i):
    if i+m > n: return False
    for k in range(m):
        if not (s[i+k] == t[k] or s[i+k] == "#"):
            return False
    return True

for i in range(n-m+1):
    if ok(i):
        s[i:i+m] = ["#"] * m

s = s[::-1]
t = t[::-1]

for i in range(n-m+1):
    if ok(i):
        s[i:i+m] = ["#"] * m

if s.count('#') == n:
    print('Yes')
else:
    print('No')