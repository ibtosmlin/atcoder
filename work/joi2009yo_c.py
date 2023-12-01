# https://atcoder.jp/contests/joi2009yo/tasks/joi2009yo_c
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1
n = int(input())
A = [int(input())-1 for _ in range(n)]

def calc(X):
    que = []
    for x in X:
        if que and que[-1]%10 != x and que[-1]//10 >= 4:
            que.pop()
        if que and que[-1]%10 == x:
            que[-1] += 10
        else:
            que.append(10 + x)

    if que and que[-1]//10 >= 4:
        que.pop()

    ret = 0
    for v in que:
        ret += v//10
    return ret

ret = 10000
for i in range(n):
    nw = A[i]
    for j in range(3):
        A[i] = j
        ret = min(ret, calc(A))
    A[i] = nw
print(ret)
