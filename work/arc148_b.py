def end(r=-1): print(r); exit()

n = int(input())
s = input()

if not 'p' in s:
    end(s)
f = s.index('p')
mx = s[:]
s0 = s[:f]
for i in range(f, n):
    ti = s[f:i+1].translate(str.maketrans({'p':'d', 'd': 'p'}))
    mx = min(mx, s0 + ti[::-1] + s[i+1:])


end(mx)
