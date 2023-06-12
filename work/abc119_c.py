n, a, b, c = map(int, input().split())
L = [int(input()) for _ in range(n)]

ret = float('inf')

def dfs(i, p, q, r):
    global ret
    if i == n:
        cost = 0
        if len(p) == 0: return
        cost += abs(sum(L[j] for j in p) - a) + (len(p) - 1) * 10
        if len(q) == 0: return
        cost += abs(sum(L[j] for j in q) - b) + (len(q) - 1) * 10
        if len(r) == 0: return
        cost += abs(sum(L[j] for j in r) - c) + (len(r) - 1) * 10
        ret = min(cost, ret)
        return
    dfs(i+1, p, q, r)
    dfs(i+1, p | {i}, q, r)
    dfs(i+1, p, q | {i}, r)
    dfs(i+1, p, q, r | {i})
    return

dfs(0, set(), set(), set())

print(ret)