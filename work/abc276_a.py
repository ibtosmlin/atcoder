# https://atcoder.jp/contests/abc276/tasks/abc276_a
s = input()[::-1]
n = len(s)
for i, si in enumerate(s):
    if si == 'a':
        print(n - i)
        exit()
print(-1)