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

from collections import defaultdict

n, k = map(int, input().split())
a = list(map(int, input().split()))
cnt = defaultdict(int)

for ai in a:
    for x in make_divisors(ai):
        cnt[x] += 1

ret = 0
for x, v in cnt.items():
    if cnt[x] >= k:
        ret = max(x, ret)
print(ret)
