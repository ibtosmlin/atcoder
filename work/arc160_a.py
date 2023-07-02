# https://atcoder.jp/contests/arc160/tasks/arc160_a
import sys
sys.setrecursionlimit(10001000)
def input(): return sys.stdin.readline().rstrip()
def int1(x): return int(x)-1

n, k = map(int, input().split())
A = list(map(int1, input().split()))

def f(A):
    