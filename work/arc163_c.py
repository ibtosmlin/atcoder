# https://atcoder.jp/contests/arc163/tasks/arc163_c

A = [i * (i+1) for i in range(1, 501)]

def f(x):
    if x == 1:
        return [1]
    elif x == 2:
        return False
    elif x in A:
        return [2] + [2*v for v in f(x-1)]
    else:
        return A[:x-1] + [x]


T = int(input())
for _ in range(T):
    ret = f(int(input()))
    if ret == False:
        print('No')
    else:
        print('Yes')
        print(" ".join(map(str, ret)))

