# https://atcoder.jp/contests/arc160/tasks/arc160_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
# import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
sys.setrecursionlimit(10001000)
int1=lambda x: int(x) - 1

N, K = map(int, input().split())
A = list(map(int1, input().split()))
B = [N-1-ai for ai in A]
dicA = {v:i for i, v in enumerate(A)}
dicB = {v:i for i, v in enumerate(B)}

def switch(l, r, X):
    return X[:l] + X[l:r+1][::-1] + X[r+1:]

used = [False] * N
cnt = K
for l, lv in enumerate(A):
    for rv in range(lv):
        r = dicA[rv]
        if used[rv]: continue
        cnt -= 1
        if cnt == 0:
            ret = switch(l, r, A)
            print(*[v+1 for v in ret])
            exit()
    used[lv] = True


used = [False] * N
cnt = N*(N+1)//2 - K + 1
for l, lv in enumerate(B):
    for rv in range(lv):
        r = dicB[rv]
        if used[rv]: continue
        cnt -= 1
        if cnt == 0:
            ret = switch(l, r, B)
            print(*[N-v for v in ret])
            exit()
    used[lv] = True

print(*[v+1 for v in A])