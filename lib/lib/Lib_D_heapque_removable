#name#
# 削除機能付きheapque
#description#
# 削除機能付きheapque
#body#
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
############

#prefix#
# Lib_D_heapque
#end#
