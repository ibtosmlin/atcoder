# https://atcoder.jp/contests/abc338/tasks/abc338_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

n = int(input())
Q = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))
mx = max(Q)

ret = 0
for x in range(mx+1):
    y = 10 ** 20
    for qi, ai, bi in zip(Q, A, B):
        ri = qi - ai * x
        if ri < 0:
            y = -1
            break
        if bi == 0: continue
        y = min(y, ri // bi)
    if y >= 0:
        ret = max(x + y, ret)
    else:
        break
print(ret)
