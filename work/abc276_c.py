# https://atcoder.jp/contests/abc276/tasks/abc276_c
n = int(input())
P = list(map(int, input().split()))
nw = 110
for i in range(n)[::-1]:
   if nw > P[i]:
      nw = P[i]
   else:
      k = i
      break

for j in range(k+1, n)[::-1]:
   if P[j] < P[k]:
      P[j], P[k] = P[k], P[j]
      break

ret = P[:k+1] + P[k+1:][::-1]
print(*ret)