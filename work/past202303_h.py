# https://atcoder.jp/contests/past202303-open/tasks/past202303_h
from collections import defaultdict
n = int(input())
A = list(map(int, input().split()))
CA = defaultdict(int)
for ai in A: CA[ai] += 1

ret = 0
for ai in sorted(CA.keys()):
    res = min(CA[ai], CA[ai+1], CA[ai+2])
    CA[ai] -= res
    CA[ai+1] -= res
    CA[ai+2] -= res
    ret += CA[ai]
print(ret)
