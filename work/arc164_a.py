# https://atcoder.jp/contests/arc164/tasks/arc164_a

def solv(x, k):
    ret = 0
    while x:
        ret += x % 3
        x //= 3
    if ret > k: return False
    if ret == k: return True
    return ret % 2 == k %2


t = int(input())
for _ in range(t):
    x, k = map(int, input().split())
    ret = solv(x, k)
    print('Yes' if ret else 'No')

