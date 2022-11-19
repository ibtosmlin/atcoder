mod = 10 ** 9 + 7
x, y = map(int, input().split())
# returns x+y! // y! x!

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

cmb = Combination(x+y)
print(cmb.nCr(x))
