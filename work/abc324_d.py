# https://atcoder.jp/contests/abc324/tasks/abc324_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

n = int(input())
S = list(map(int, list(input())))
S.sort(reverse=True)
mx = 0
cntS = [0] * 10
for si in S:
    mx *= 10
    mx += si
    cntS[si] += 1

ret = 0
for i in range(0, 4*10**7):
    x = i * i
    if mx < x: break
    cntT = [0] * 10
    for i in range(n):
        cntT[x%10] += 1
        x //= 10
    if cntS == cntT: ret += 1
print(ret)
