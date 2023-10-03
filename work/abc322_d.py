# https://atcoder.jp/contests/abc322/tasks/abc322_d
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

def inpol():
    ret = [list(input()) for _ in range(4)]
    mi = 4
    mj = 4
    for i in range(4):
        for j in range(4):
            if ret[i][j] == "#":
                ret[i][j] = 1
                mi = min(mi, i)
                mj = min(mj, j)
            else:
                ret[i][j] = 0
    sret = [[0] * 4 for _ in range(4)]
    for i in range(mi, 4):
        for j in range(mj, 4):
            sret[i-mi][j-mj] = ret[i][j]
    return sret

def rotate(A):
    A = [list(x) for x in zip(*A[::-1])]
    mi = 4
    mj = 4
    for i in range(4):
        for j in range(4):
            if A[i][j] == 1:
                mi = min(mi, i)
                mj = min(mj, j)
    sret = [[0] * 4 for _ in range(4)]
    for i in range(mi, 4):
        for j in range(mj, 4):
            sret[i-mi][j-mj] = A[i][j]
    return sret


def check(p0, p1, p2, si0, sj0, si1, sj1, si2, sj2):
    ret = [[0] * 4 for _ in range(4)]
    def make(A, i, j):
        for u in range(4):
            for v in range(4):
                if i + u < 4 and j + v < 4:
                    ret[i+u][j+v] += A[u][v]
                    if ret[i+u][j+v] >= 2: return False
                else:
                    if A[u][v]: return False
        return True
    if make(p0, si0, sj0) == False: return False
    if make(p1, si1, sj1) == False: return False
    if make(p2, si2, sj2) == False: return False
    for i in range(4):
        for j in range(4):
            if ret[i][j] != 1: return False
    return True

p0 = inpol()
p1 = inpol()
p2 = inpol()

from itertools import *
PN = list(product(range(4), repeat=6))

for t1 in range(4):
    p1 = rotate(p1)
    for t2 in range(4):
        p2 = rotate(p2)

        for si0, sj0, si1, sj1, si2, sj2 in PN:
            if check(p0, p1, p2, si0, sj0, si1, sj1, si2, sj2):
                exit(print('Yes'))
print('No')
