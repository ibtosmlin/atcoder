# https://atcoder.jp/contests/ttpc2019/tasks/ttpc2019_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1


##############################
# 素数出力 O(n**0.5)
# n <= 10**5
##############################
def get_primes(n:int) -> list:
# n以下の素数列挙
    n += 1
    IsPrime = [True] * n
    IsPrime[0], IsPrime[1] = False, False
    for p in range(n):
        if not IsPrime[p]: continue
        for j in range(p*2, n, p):
            IsPrime[j] = False
    ret = [p for p in range(n) if IsPrime[p]]
    return ret

n = int(input())
x = list(map(int, input().split()))
m = max(x)
gs = [0] * (m+1)
ps = get_primes(m)
for i in range(len(ps)):
    if i and ps[i] - ps[i-1] == 2:
        gs[ps[i]] = gs[ps[i-1]] + 1
    else:
        gs[ps[i]] = 1

# print(gs[:30])

mx = 0
for xi in x:
    mx ^= gs[xi]

if mx != 0:
    print('An')
else:
    print('Ai')