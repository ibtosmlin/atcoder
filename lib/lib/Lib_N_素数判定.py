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

#prefix#
# Lib_N_prime_素数
#end#
