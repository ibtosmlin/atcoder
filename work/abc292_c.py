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


n = int(input())
cnt = [-1] * (n+1)
ret = 0
for i in range(1, n):
    j = n-i
    if cnt[i] == -1:
        cnt[i] = len(make_divisors(i))
    if cnt[j] == -1:
        cnt[j] = len(make_divisors(j))
    ret += cnt[i] * cnt[j]
print(ret)