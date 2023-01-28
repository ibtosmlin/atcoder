x, a, b, c = map(int, input().split())

# x/b < x/a + c -> Tortoise
if x*a - x*b < a*b*c:
    print('Tortoise')
elif x*a - x*b > a*b*c:
    print('Hare')
else:
    print('Tie')