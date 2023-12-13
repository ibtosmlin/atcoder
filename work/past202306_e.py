# https://atcoder.jp/contests/past15-open/tasks/past202306_e
N, K = map(int, input().split())
a = list(map(int, input().split()))
# N-1 K-1選ぶ
C = 1
for i in range(1, K):
    C *= (N-i)
for i in range(1, K):
    C //= i
print(C*sum(a))
