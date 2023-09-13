from itertools import *
A = []
for _ in range(3): A += list(map(int, input().split()))
seqs = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]

def _check(p, seq):
    od = [A[q] for q in p if q in seq]
    if od[0] == od[1] != od[2]: return False
    return True

def check(p):
    for seq in seqs:
        if not _check(p, seq): return False
    return True

ret = 0
for p in permutations(range(9)):
    if check(p): ret+=1

print(ret/362880)

