s = list(input())
for i in range(len(s)//2):
    s[i*2], s[i*2+1] = s[i*2+1], s[i*2]
print(''.join(s))