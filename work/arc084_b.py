# https://atcoder.jp/contests/math-and-algorithm/tasks/arc084_b
from collections import deque
INF = 10**10
k = int(input())
cost = [INF] * k
que = deque()
cost[1] = 0
que.append(1)
while que:
    x = que.popleft()
    d = cost[x]
    # x10
    nx = (x*10)%k
    if cost[nx] > d:
        cost[nx] = d
        que.appendleft(nx)
    # +1
    nx = (x+1)%k
    if cost[nx] > d+1:
        cost[nx] = d + 1
        que.append(nx)
print(cost[0]+1)