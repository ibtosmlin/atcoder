# XOR の性質
定義
- a = 0, b = 0 -> xor(a,b)= 0
- a = 1, b = 0 -> xor(a,b)= 1
- a = 0, b = 1 -> xor(a,b)= 1
- a = 1, b = 1 -> xor(a,b)= 0

可換
- a ^ b == b ^ a

結合
- (a ^ b) ^ c == a ^ (b ^ c)

逆元
- a ^ x ^ x == a
- a ^ x == b ^ x  <=> a == b            // ^x を作用させる
- a != b          <=> a ^ x != b ^ x    // ^x を作用させる

通常和との関係
- a ^ b <= a + b        // 桁の繰上りがxorにはない
- // 一致するときは繰上りがないつまり同じ桁に1,1となることはない

任意の偶数 n についてn ^ (n+1) = 1

0^1^...^(x-1)^x 累積xor
def g(x):
    if x % 4 == 0:
        return x
    elif x % 4 == 1:
        return 1
    elif x % 4 == 2:
        return 1 ^ x
    elif x % 4 == 3:
        return 0