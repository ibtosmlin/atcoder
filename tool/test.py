def BubbleSort(A, N):
    # 後ろから大きいものを前にスワップしていく
    flag = True
    cnt = 0
    while flag:
        flag = False
        for i in range(1, N)[::-1]:
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]
                cnt += 1
                flag = True
    return A, cnt

def SelectionSort(A, N):
    # 前から最小値を見つけてスワップしていく
    cnt = 0
    for i in range(N):
        minpos = i
        for j in range(i+1, N):
            if A[j] < A[minpos]:
                minpos = j
        if i != minpos:
            A[i], A[minpos] = A[minpos], A[i]
            cnt += 1
    return A, cnt

class Card:
    def __init__(self, s:str):
        self.type = s[0]
        self.value = int(s[1:])
        self.card = s

    def __lt__(self, other):
        return self.value < other.value



n = int(input())
X = list(input().split())

BSA, _ = BubbleSort(list(map(Card, X)), n)
SSA, _ = SelectionSort(list(map(Card, X)), n)

BSA = [c.card for c in BSA]
SSA = [c.card for c in SSA]

print(*BSA)
print('Stable')
print(*SSA)
if BSA == SSA:
    print('Stable')
else:
    print('Not stable')