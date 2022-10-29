n = int(input())
a = list(map(int, input().split()))
ret = 0
for ai in a:
    ret += ai
    ret %= 100
print(ret)