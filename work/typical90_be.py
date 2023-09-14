# https://atcoder.jp/contests/typical90/tasks/typical90_be
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1


mod = 998244353
n, m = map(int, input().split())
mat = [[0] * n for _ in range(m)]
for j in range(n):
    _t = int(input())
    for i in map(lambda x: int(x)-1, input().split()):
        mat[i][j] = 1
s = list(map(int, input().split()))


def solve_linear_equation(A, b):
    """A・x = b となるxを見つける"""
    h, w = len(A), len(A[0])
    """extend"""
    _A = []
    for Ai, bi in zip(A, b):
        _A.append(Ai + [bi])
    rank = 0
    for col in range(w):
        for row in range(rank, h):
            if _A[row][col]:
                _A[row], _A[rank] = _A[rank], _A[row]
                break
        else: continue
        for row in range(h):
            if row != rank and _A[row][col]:
                for _col in range(w + 1):
                    _A[row][_col] ^= _A[rank][_col]
        rank += 1
    # for ai in A: print(ai)
    # print("---")
    # for ai in _A: print(ai)
    # print(rank)
    return _A, rank

A, rank = solve_linear_equation(mat, s)
for r in range(rank, m):
    if A[r][n]:
        exit(print(0))
print(pow(2, n-rank, mod))
