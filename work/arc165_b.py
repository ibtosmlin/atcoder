# https://atcoder.jp/contests/arc165/tasks/arc165_b
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

###################################

n, k = map(int, input().split())
p=list(map(int, input().split()))

inc = [0]
for i in range(n):
    if p[i] > p[i-1]:
        inc.append(inc[-1]+1)
    else:
        inc.append(inc[-1])

for i in range(n-k+1):
    last = 0
    if inc[k+i] - inc[i] >= k-1:
        print(*p)
        exit()

j = 0
for i in range(n-k)[::-1]:
    if p[i] < p[i+1]:
        j+=1
    else:
        break
print(*(p[:n-(k+j)] + sorted(p[n-(k+j):n-j]) + p[n-j:]))


# print(inc)