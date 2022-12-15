while True:
    n, k = map(int, input().split())
    if n == k == 0: break
    x = list(map(int, input().split()))
    x.sort()
    now = 0
    print(sum(x[:k]))
    
