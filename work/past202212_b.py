a, b, c, d = map(int, input().split())
if b*d>0:
    if a*d < c* b:
        print('<')
    elif a*d > c*b:
        print('>')
    else:
        print('=')
else:
    if a*d < c* b:
        print('>')
    elif a*d > c*b:
        print('<')
    else:
        print('=')
