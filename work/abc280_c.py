# https://atcoder.jp/contests/abc280/tasks/abc280_c
s = input() + '9'
t = input()
for i in range(len(t)):
    if s[i] != t[i]:
        print(i+1)
        break
