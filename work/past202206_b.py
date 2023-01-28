from collections import Counter
s = input()
n = len(s)
x = [s[i:i+2] for i in range(n-1)]
X = Counter(x)

m = 0
r = ''
for k, v in X.items():
    if v > m:
        m = v; r = k
    elif v == m:
        if k < r:
            r = k
print(r)