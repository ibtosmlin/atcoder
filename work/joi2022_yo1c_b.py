s = int(input())
a = int(input())
b = int(input())
t = 250
s -= a
while s > 0:
    t += 100
    s -= b
print(t)
