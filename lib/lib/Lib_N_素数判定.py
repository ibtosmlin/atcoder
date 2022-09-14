#name#
# 素数判定・出力
#descripiton#
# 素数判定・出力
#body#

##############################
# 素数判定 O(n**0.5)
##############################
def is_prime(n:int) -> bool:
    if n in {0, 1}: return False
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


##############################
# n以下の素数の数 O(n**0.5)
# n ～ 10**10 for python3
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


#prefix#
# Lib_N_prime_素数
#end#
