N, R = map(int, input().split())
S = list(input())
i = 0
ret = 0
while '.' in S[i:]:
    if not "." in S[i+R:]:
        ret += 1
        ret += i
        break
    elif S[i]==".":
        ret += 1
        for j in range(R):
            if i+j<N:
                S[i+j] = 'o'
    i += 1
print(ret)
