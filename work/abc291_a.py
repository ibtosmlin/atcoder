# https://atcoder.jp/contests/abc291/tasks/abc291_a
s = input()
f = ord("A")
e = ord("Z")
for i, si in enumerate(s):
    if f <= ord(si) <=e:
        print(i+1)
        break
