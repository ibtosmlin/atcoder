def sumstr(x: str, y: str):
    signx = x[0] == '-'
    signy = y[0] == '-'
    if signx == signy:
        return sumstr()

t = int(input())
for _ in range(t):
    a, b = map(int, input().split())