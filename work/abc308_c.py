# https://atcoder.jp/contests/abc308/tasks/abc308_c

class ordobj:
    def __init__(self, x):
        self.a, self.b, self.i = x

    def __lt__(self, other):
        if self.a * (other.a+other.b) < other.a * (self.a+self.b):
            return True
        if self.i > other.i:
            return True
        return False

    def __repr__(self):
        return f'{self.a} {self.b} {self.i}'
########################################

n = int(input())
x = []
for i in range(n):
    u, v = map(int, input().split())
    x.append(ordobj((u, v, i+1)))

x.sort(reverse=True)

ret = []
for xi in x:
    ret.append(xi.i)
print(*ret)

