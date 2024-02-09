# https://atcoder.jp/contests/abc338/tasks/abc338_d
int1=lambda x: int(x) - 1
n, m = map(int, input().split())
X = list(map(int1, input().split()))
P = [0] * (n+1)
ret = 0
for i in range(m-1):
    l, r = X[i:i+2]
    if l > r: l, r = r, l
    d = r - l
    ret += d
    dd = n - d - d
    P[l] += dd
    P[r] -= dd

for i in range(1, n):
    P[i] += P[i-1]

print(ret+ min(P))
