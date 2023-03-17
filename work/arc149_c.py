ret3 = [
    5,3,1,
    9,7,8,
    6,2,4
    ]
ret4 = [
        1,3,5,7,
        9,11,13,15,
        12,10,8,6,
        4,2,16,14
        ]
ret5 = [
    1,3,5,7,9,
    11,13,15,19,17,
    21,23,25,2,4,
    6,10,8,12,14,
    16,18,20,22,24
    ]

n = int(input())

if n == 3: ret = ret3
elif n == 4: ret = ret4
elif n == 5: ret = ret5
else:
    odd = list(range(1, n*n+1, 2))
    even = list(range(2, n*n+1, 2))
    odd.sort(key=lambda x: x%3, reverse=True)
    even.sort(key=lambda x: x%3)
    ret = odd + even

for i in range(n):
    print(*ret[i*n:i*n+n])