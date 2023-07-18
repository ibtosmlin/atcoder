s = input()
now = 0
for si in s:
    if si == '(':
        now += 1
    elif si == ')':
        now -= 1
    if now < 0:
        exit(print('No'))
if now == 0:
    print('Yes')
else:
    print('No')
