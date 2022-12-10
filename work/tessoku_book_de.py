n, k = map(int, input().split())
a = list(map(int, input().split()))
ret = [False] * (n+1)
for i in range(1, n+1):
    for ai in a:
        if i-ai >= 0 and not ret[i-ai]:
            ret[i] = True
            break
if ret[-1]:
    print('First')
else:
    print('Second')
#print(ret)