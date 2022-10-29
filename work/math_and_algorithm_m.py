n = int(input())
div = set()
for d in range(1, int(n**0.5)+1):
    if n%d==0:
        div.add(d)
        div.add(n//d)
for d in div:
    print(d)