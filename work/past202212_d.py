n, m = map(int, input().split())
s=input()
ret = [0] * n
now = 0
for i in range(m):
    ret[i%n] += 1
    if s[i] == '+':
        ret[i%n] += now
        now = 0
    elif s[i] == '-':
        now += ret[i%n]
        ret[i%n] = 0
print('\n'.join(map(str, ret)))