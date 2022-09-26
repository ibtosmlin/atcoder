# https://atcoder.jp/contests/abc270/tasks/abc270_b
def end(r=-1): print(r); exit()
x, y, z = map(int, input().split())
if x < 0:
    x *= -1
    y *= -1
    z *= -1

if y < 0 or y > x: end(x)
# 以下 0 < y < x
if y < z: end(-1)   # 0 < y < z < x
if z > 0: end(x)    # 0 < z < y < x
end(2*abs(z) + x)   # z < 0 < y < x
