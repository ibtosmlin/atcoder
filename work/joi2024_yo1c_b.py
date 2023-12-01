# https://atcoder.jp/contests/joi2024yo1c/tasks/joi2024_yo1c_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
a = int(input())
b = int(input())
def d(x):
    cnt = 0
    while x:
        x //= 10
        cnt += 1
    return cnt
print(d(a+b))