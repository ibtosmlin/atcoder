# https://atcoder.jp/contests/past16-open/tasks/past202309_j
import sys; input: lambda _: sys.stdin.readline().rstrip()
import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
from math import gcd

n, k = map(int, input().split())
A = list(map(int, input().split()))
D = set()
for i in range(k-1):
    D.add(A[i+1]-A[i])
D = sorted(D)
g = D[0]
for di in D:
    g = gcd(g, di)

##############################
# 約数列挙 O(n**0.5)
# returns sorted list
##############################
def make_divisors(n:int) -> list:
    lower_divisors, upper_divisors = [], []
    for i in range(1, int(n**0.5)+1):
        if n % i != 0: i += 1; continue
        lower_divisors.append(i)
        j = n // i
        if i != j: upper_divisors.append(j)
    return lower_divisors + upper_divisors[::-1]

kouho = make_divisors(g)

ret = []
for p in kouho:
    if (A[-1] - A[0]) // p < n:
        ret.append(p)

print(len(ret))
print(*ret)