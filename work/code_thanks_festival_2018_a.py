t, a, b, c, d = map(int, input().split())
ret = [0]
if t >= a + c:
    ret.append(b + d)
if t >= a:
    ret.append(b)
if t >= c:
    ret.append(d)
print(max(ret))