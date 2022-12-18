ret = 0
for _ in range(3):
    ret += int(input())
s = int(input())
if ret <= s <= ret+3:
    print('Yes')
else:
    print('No')
