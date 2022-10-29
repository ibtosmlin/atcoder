n = input()
f = 0
for si in n:
    f += int(si)

c, r = divmod(f, 9)
ret = str(r) + '9' * c
ret = str(int(ret))
if ret != n:
    print(ret)
else:
    if r == 0:
        print('18' + ret[1:])
    elif c >= 1:
        print(str(r+1) + '8' + ret[2:])
    else:   #c == 0
        print(10 + r-1)
