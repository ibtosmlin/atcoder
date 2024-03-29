#title#
# 素数判定・出力

#subtitle#
# is_prime(n):素数判定 O(n**0.5)
# miller_rabin(n):素数ミラーラビン判定 n < 10**18, Q = 10**5回
# get_prime(n):n以下の素数出力 O(n**0.5)
# count_primes(n):n以下の素数の数 O(n**0.5)


#name#
# 素数判定・出力
#descripiton#
# 素数判定・出力
#body#

##############################
# 素数判定 O(n**0.5)
##############################
def is_prime(n:int) -> bool:
    if n <= 1: return False
    if n == 2: return True
    if n % 2 == 0: return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0: return False
    return True

#####################
print(10, is_prime(10))
print(31, is_prime(31))
#####################


##############################
# 素数ミラーラビン判定
# N < 10**18, Q = 10**5回
##############################

from random import randint as ri

def miller_rabin(N, Times=10):
    if N == 2: return True
    if N == 1 or N%2 == 0: return False

    q = N-1
    k = 0
    while q&1==0:
        q >>= 1
        k += 1

    for _ in range(Times):
        m = ri(2, N-1)
        y = pow(m, q, N)
        if y == 1: continue

        for _ in range(k):
            if (y+1) % N == 0: break
            y = y * y % N

        else: return False
    return True


for _ in range(int(input())):
    n = int(input())
    print('Yes' if miller_rabin(n, 10) else 'No')


##############################
# 素数出力 O(n**0.5)
# n <= 10**5
##############################
def get_primes(n:int) -> list:
# n以下の素数列挙
    n += 1
    IsPrime = [True] * n
    IsPrime[0:2] = [False, False]
    for p in range(n):
        if not IsPrime[p]: continue
        for j in range(p*2, n, p):
            IsPrime[j] = False
    ret = [p for p in range(n) if IsPrime[p]]
    return ret


##############################
# n以下の素数の数 O(n**0.5)
# n ～ 10**12 for pypy3
##############################
def count_primes(n:int):
    if n < 2:
        return 0
    v = int(n ** 0.5) + 1
    smalls = [i // 2 for i in range(1, v + 1)]
    smalls[1] = 0
    s = v // 2
    roughs = [2 * i + 1 for i in range(s)]
    larges = [(n // (2 * i + 1) + 1) // 2 for i in range(s)]
    skip = [False] * v

    pc = 0
    for p in range(3, v):
        if smalls[p] <= smalls[p - 1]:
            continue

        q = p * p
        pc += 1
        if q * q > n:
            break
        skip[p] = True
        for i in range(q, v, 2 * p):
            skip[i] = True

        ns = 0
        for k in range(s):
            i = roughs[k]
            if skip[i]:
                continue
            d = i * p
            larges[ns] = larges[k] - \
                (larges[smalls[d] - pc] if d < v else smalls[n // d]) + pc
            roughs[ns] = i
            ns += 1
        s = ns
        for j in range((v - 1) // p, p - 1, -1):
            c = smalls[j] - pc
            e = min((j + 1) * p, v)
            for i in range(j * p, e):
                smalls[i] -= c

    for k in range(1, s):
        m = n // roughs[k]
        s = larges[k] - (pc + k - 1)
        for l in range(1, k):
            p = roughs[l]
            if p * p > m:
                break
            s -= smalls[m // p] - (pc + l - 1)
        larges[0] -= s

    return larges[0]


##############################
# n!が素数pで何回割れるか O(logn)
# legendre(n, p)
##############################
def legendre(n, p):
    ret = 0
    while n > 0:
        ret += n // p
        n //= p
    return ret

#prefix#
# Lib_N_prime_素数
#end#
