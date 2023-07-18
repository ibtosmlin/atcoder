n = int(input())
a, b, c, d = map(int, input().split())
x = input()
x = int(x.replace('.', ''))

def isok(u):
    #
    # (a + b*2 + c*3 +d*4 + u) / (a+b+c+d+ u) <= x
    # (a*1000 + b*2000 + c*3000 +d*4000 + u*1000) / (a+b+c+d+ u) <= x
    # a*1000 + b*2000 + c*3000 +d*4000 + u*1000 <= x * (a+b+c+d+ u)
    return (a + b*2 + c*3 + d*4) * 1000 - x * (a+b+c+d) <= (x-1000)* u

if isok(0):
    print(0)
    exit()


r = 10**18
l = 0
while r - l > 1:
    mid = (r+l)//2
    if isok(mid):
        r = mid
    else:
        l = mid
print(r)
