# https://atcoder.jp/contests/agc064/tasks/agc064_a
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1

n = int(input())
L = n * (n+1) // 2

num = [i for i in range(n+1)]

ret = [1]
num[1] = 0

def dfs(num, ret):
    # print(num, ret)
    x = ret[-1]
    if len(ret) == L:
        return abs(x - ret[0]) in [1, 2]
    for nx in range(x-2, x+3):
        if nx == x: continue
        if not (1 <= nx <= n): continue
        if num[nx] == 0: continue
        num[nx] -= 1
        ret.append(nx)
        if dfs(num, ret) == True:
            return True
        else:
            num[nx] += 1
            ret.pop()
    return False

dfs(num, ret)
print(*ret)
