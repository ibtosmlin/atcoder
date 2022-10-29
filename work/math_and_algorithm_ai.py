n, q = map(int, input().split())
a = list(map(int, input().split()))
ra = [0]
for ai in a:
    ra.append(ra[-1] + ai)
for _ in range(q):
    l, r = map(int, input().split())
    l -= 1
    print(ra[r]-ra[l])