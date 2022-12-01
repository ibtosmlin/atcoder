n = int(input())
c = [0] * 100
for ai in input().split():
    c[int(ai)%100] += 1

ret = 0
for i in range(1, 50):
    ret += c[i] * c[100-i]
ret += c[0] * (c[0]-1) // 2
ret += c[50] * (c[50]-1) // 2
print(ret)