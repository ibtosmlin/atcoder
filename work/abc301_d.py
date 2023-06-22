# https://atcoder.jp/contests/abc301/tasks/abc301_d
s = list(input())
n = int(input())

def val(s):
    ret = 0
    for si in s:
        ret *= 2
        if si == '1': ret += 1
    return ret

if val(s) > n:
    print(-1)
    exit()

while s.count('?'):
    i = s.index('?')
    s[i] = "1"
    if val(s) <= n:
        continue
    else:
        s[i] = "0"

print(val(s))
