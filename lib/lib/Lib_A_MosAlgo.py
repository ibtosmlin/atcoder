#name#
# Mo'sAlgorythm#
#description#
# Mo'sAlgorythm#
#body#

# A:リスト n = 10**5
# Q: l, r q = 10**5

class _Mo:
    def __init__(self, N:int):
        self.N=N
        self.query = []
        self.Q = 0
        self.shift = 20
    def add_query(self, l:int, r:int): # [l,r)
        self.query.append((l,r))
        self.Q += 1
    def solve(self):
        assert max(self.N, self.Q)<(1<<self.shift)
        block_size = self.N // (min(self.N, int(len(self.query)**0.5+0.5)))
        query = [None] * self.Q
        for i,(l,r) in enumerate(self.query):
            L = l // block_size
            query[i] = (L<<(2*self.shift))+((r if L&1 else -r)<<self.shift) + i
        query.sort()
        L=R=0
        ret = [0]*self.Q
        mask=(1<<self.shift)-1
        for q in query:
            i = q&mask
            l,r=self.query[i]
            while l<L:
                L-=1;
                self.add_left(L)
            while L<l:
                self.remove_left(L)
                L+=1
            while R<r:
                self.add_right(R)
                R+=1
            while r<R:
                R-=1
                self.remove_right(R)
            ret[i] = self.get_state()
        return ret

N,Q=map(int,input().split())
A=list(map(int,input().split()))

class Mo(_Mo):
    def __init__(self, N):
        super().__init__(N)
        self.value = 0
        self.count = [0] * (max(A)+1)
    def get_state(self):
        return self.value
    def add_left(self, i):
        a = A[i]
        x = self.count[a]
        self.count[a] += 1
#        self.value += (x+1)*x*(x-1) // 6 - x*(x-1)*(x-2) // 6
        self.value += x*(x-1) // 2
    def remove_left(self, i):
        a = A[i]
        x = self.count[a]
        self.count[a] -= 1
#        self.value += (x-1)*(x-2)*(x-3) // 6 - x*(x-1)*(x-2) // 6
        self.value -= (x-1)*(x-2)//2

    add_right = add_left
    remove_right = remove_left


mo = Mo(N)
for _ in range(Q):
    l,r=map(int,input().split())
    mo.add_query(l-1,r)
ans = mo.solve()

print("\n".join(map(str,ans)))


#prefix#
# Lib_Mos_モアルゴリズム
#end#
