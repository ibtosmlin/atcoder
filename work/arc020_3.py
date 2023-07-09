# https://atcoder.jp/contests/arc020/tasks/arc020_3

n = int(input())
nums = [tuple(map(int, input().split())) for _ in range(n)]
mod = int(input())

ret = 0
for a, l in nums:
    la = len(str(a))
    mul = a
    shift = pow(10, la, mod)
    while l:
        if l % 2:
            ret = (ret * shift + mul) % mod
        mul = (mul * shift + mul) % mod
        shift = shift * shift % mod
        l //= 2

print(ret)
