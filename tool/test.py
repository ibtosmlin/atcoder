n=int(input())
s=input().split("<")
r=0
for u in s:
    w = len(u)
    r += w * (w+1) // 2
print(r)