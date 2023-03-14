# https://atcoder.jp/contests/abc293/tasks/abc293_b
def int1(x): return int(x)-1
n = int(input())
a = list(map(int1, input().split()))
seen = [False] * n
for i, ai in enumerate(a):
    if seen[i]: continue
    seen[ai] = True
ret = [i+1 for i in range(n) if not seen[i]]
print(len(ret))
print(*ret)