# RULD -> 0,1,2,3
direcStr = 'RULD'
direcMove = [(1, 0), (0, 1), (-1, 0), (0, -1)]
Points = dict()

class Point:
    def __init__(self, x, y):
        self.Next = [(x+dx, y+dy) for dx, dy in direcMove]
        for i in range(4):
            if self.Next[i] in Points:
                self.Next[i] = Points[self.Next[i]].Next[i]

def Visit(pos: tuple):
    if pos in Points:
        

    else:
        Points[pos] = Point(*pos)

Visit((0, 0))



k = int(input())
s = input()
now = (0, 0)
for si in s:
    di = direcStr.index(si)
    now = NextTo(now, di)
    Visit(now)

print(*now)
