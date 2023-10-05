#title#
# 削除機能付きheapque
#subtitle#
# DeletableMaxMinHeapQ: クラス
# heappush:
# heappopmax: 大きいものを取り出す
# heappopmin: 小さいものを取り出す
# heapmax: 大きいものにアクセス
# heapmin: 小さいものにアクセス
# heapdel(x): xを削除

#name#
# 削除機能付きheapque
#description#
# 削除機能付きheapque
#body#
from heapq import heappush, heappop
from collections import defaultdict
class DeletableMaxMinHeapQ():
    def __init__(self):
        self.Hma = []
        self.Hmi = []
        self.HC = defaultdict(int)
    def heappush(self, x):
        heappush(self.Hma, -x)
        heappush(self.Hmi, x)
        self.HC[x] += 1
    def heappopmax(self):
        t = -heappop(self.Hma)
        while not self.HC[t]:
            t = -heappop(self.Hma)
        self.HC[t] -= 1
        return t
    def heappopmin(self):
        t = heappop(self.Hmi)
        while not self.HC[t]:
            t = heappop(self.Hmi)
        self.HC[t] -= 1
        return t
    def heapmax(self):
        t = -self.Hma[0]
        while not self.HC[t]:
            heappop(self.Hma)
            t = -self.Hma[0]
        return t
    def heapmin(self):
        t = self.Hmi[0]
        while not self.HC[t]:
            heappop(self.Hmi)
            t = self.Hmi[0]
        return t
    def heapdel(self, x):
        assert self.HC[x] > 0
        self.HC[x] -= 1
    def __contains__(self, x):
        return 1 if x in self.HC and self.HC[x] else 0

hq = DeletableMaxMinHeapQ()
n, q = map(int, input().split())
a = list(map(int, input().split()))
for ai in a:
    hq.heappush(ai)

for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        hq.heappush(query[1])
    elif query[0] == 1:
        x = hq.heappopmin()
        print(x)
    else:
        x = hq.heappopmax()
        print(x)


# https://judge.yosupo.jp/problem/double_ended_priority_queue

############

#prefix#
# Lib_D_heapque
#end#
