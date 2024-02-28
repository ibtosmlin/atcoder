# https://atcoder.jp/contests/abc342/tasks/abc342_d
from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))

Max = int(max(A)**0.5) + 10
IsPrime = [True] * Max
IsPrime[0], IsPrime[1] = False, False
Primes = []
for p in range(2, Max):
    if IsPrime[p]:
        Primes.append(p)
        for k in range(p*2, Max, p):
            IsPrime[k] = False

zcnt = 0
cnt = defaultdict(int)
for ai in A:
    if ai == 0:
        zcnt += 1
        continue
    for pi in Primes:
        pi2 = pi*pi
        if pi2 > ai: break
        while ai%pi2 == 0:
            ai//=pi2
    cnt[ai] += 1

ret = zcnt * (zcnt-1) // 2
if zcnt != n:
    ret += zcnt * (n-zcnt)
    for v in cnt.values():
        ret += v * (v-1) // 2
print(ret)