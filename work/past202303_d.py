# https://atcoder.jp/contests/past202303-open/tasks/past202303_d

H, A, B, C, D = map(int, input().split())

def f(h):
    if h <= 0:
        return 0
    item2 = max(h-C,0)//2 + C
    use2 = f(h-item2) + D
    use1 = ((h+(A-1))//A)*B
    return min(use1, use2)

print(f(H))