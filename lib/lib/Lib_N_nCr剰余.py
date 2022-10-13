#name#
# nCr
#description#
# nCr剰余
#body#


#####################################
# nCr % 10**9+7
#####################################
mod, lim = 10**9+7, 10**6                   # mod素数, 出力の制限
g1, g2 = [[1]*(lim+1) for _ in range(2)]    # ！と逆元tbl
for i in range(2, lim + 1):
    g1[i] = g1[i-1] * i % mod
g2[-1] = pow(g1[-1], mod-2, mod)
for i in range(lim, 0, -1):
    g2[i-1] = g2[i] * i % mod

def fac(n): return g1[n]
def facinv(n): return g2[n]
def nCr(n, r):
    """nCr
    n個のものからr個選ぶ
    """
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return fac(n) * facinv(r) * facinv(n-r) % mod

def nPr(n, r):
    """nPr
    n個のものからr個選んで並べる
    """
    if ( r<0 or r>n ):
        return 0
    return fac(n) * facinv(n-r) % mod

def nHr(n, r):
    """nHr = n-1+rCr
    n種類のものからr個重複を許して選ぶ(一個も選ばれないものがあっても可)
    (一個も選ばれないものがダメな場合はnをn-rとする・あらかじめ１個づつ選んでおく)
    """
    return nCr(n-1+r, n-1)

ret = nCr(4, 2)

class Combination:
    """nCrの前計算

    Parameters
    ----------
    n : int, optional
        n固定 by default 1
    mod : int, optional
        modの値, by default 10**9+7

    Note:
    ----------
    nCr % 10**9+7  n～10^9 r～10^5
    nは大きいが固定で,rは小さい場合
    """
    def __init__(self, n : int=10**9, mod : int=10**9+7) -> None:
        self.n = n
        self.max_r = 1
        self.mod = mod
        self.nCrseq = [1, n%mod]


    def __preprocessing(self, max_r:int) -> None:
        seq = self.nCrseq
        mod = self.mod
        seq += [0] * (max_r - self.max_r)
        for i in range(self.max_r + 1, max_r + 1):
            seq[i] = (seq[i-1] * (self.n-i+1) * pow(i,mod-2,mod)) % mod
        self.max_r = max_r


    def nCr(self, r:int) -> int:
        if r > self.max_r: self.__preprocessing(r)
        return self.nCrseq[r]

cmb = Combination(10)
print(cmb.nCr(4))



#####################################
# nCr % 3
#####################################
class combination_mod_3:
    def __init__(self):
        n = 10**6
        self.bf = [0] * n
        self.bg = [0] * n
        self.bg[0] = 1

        for i in range(1, n):
            pos = i
            while pos % 3 == 0:
                pos //= 3
                self.bf[i] += 1
            self.bg[i] = pos % 3

        for i in range(1, n):
            self.bf[i] += self.bf[i-1]
            self.bg[i] = self.bg[i] * self.bg[i-1] % 3
        self.MaxN = n

    def nCr(self, n, r):
        bf = self.bf
        if bf[n] != bf[r] + bf[n-r]: return 0
        bgn = self.bg[n]
        bgrnr = self.bg[r] * self.bg[n-r]
        if bgn == 1 and bgrnr == 1: return 1
        if bgn == 1 and bgrnr == 2: return 2
        if bgn == 1 and bgrnr == 4: return 1
        if bgn == 2 and bgrnr == 1: return 2
        if bgn == 2 and bgrnr == 2: return 1
        if bgn == 2 and bgrnr == 4: return 2
        return -1

c = combination_mod_3()
print(c.nCr(5,1))   #5mod3->2
print(c.nCr(5,2))   #10mod3->1
print(c.nCr(6,2))   #15mod3->0
print(c.nCr(6,3))   #20mod3->2

#prefix#
# Lib_N_nCr剰余
#end#
