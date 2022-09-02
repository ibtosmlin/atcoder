#name#
# 約数列挙
#descripiton#
# 約数列挙
#body#
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

#####################
print(make_divisors(10))
#####################

#prefix#
# Lib_N_約数列挙
#end#
