import math

H, W, D = map(int, input().split())
PI = math.pi
ret = PI * D * D / 4
H /= 2
W /= 2
if H > W:
    H, W = W, H

def f(x):
    r = math.acos(x/D)
    ret = D * D * r / 2 - D * x * math.sin(r) / 2
    return ret

if D * D > H * H + W * W:
    ret = H * W
elif W < D:
    ret = PI * D * D / 4 - f(H) - f(W)
elif H < D <= W:
    ret = PI * D * D / 4 - f(H)
else:
    ret = PI * D * D / 4

print(ret/(H*W))

