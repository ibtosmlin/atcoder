# name#
# Sorted Multi Set
# description#
# body#
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedMultiset.py


import math
from bisect import bisect_left, bisect_right, insort
from typing import Generic, Iterable, Iterator, TypeVar, Union, List

T = TypeVar('T')


class SortedMultiset(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size: size * (i + 1) // bucket_size] for i in range(bucket_size)]

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedMultiset from iterable. / O(N) if sorted / O(N log N)"
        a = list(a)
        if not all(a[i] <= a[i + 1] for i in range(len(a) - 1)):
            a = sorted(a)
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedMultiset" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1: len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]: return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def count(self, x: T) -> int:
        "Count the number of x."
        return self.index_right(x) - self.index(x)

    def add(self, x: T) -> None:
        "Add an element. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return
        a = self._find_bucket(x)
        insort(a, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Union[T, None]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]

    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        "sm[-1]も可能"
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans


###############################################


# prefix#
# Lib_D_sorted_multi_set
# end#
#name#
# Mo'sAlgorythm#
#description#
# Mo'sAlgorythm#
#body#

# A:リスト n = 10**5
# Q: l, r, q = 10**5
# O(NQ−−√)が間に合う条件である*3
# 区間伸縮の計算がO(1) またはそれに近い
# クエリがオフラインで与えられる(先読みができる)
# 配列の要素が不変である

class _Mo:
    def __init__(self, N:int, Q:int):
        self.N=N
        self.Q = Q
        self.shift = 20
        self.BSIZE = int(Q**0.5)+1  # bucket size
        self.data = [0] * Q
        self.query = [[] for _ in range(self.BSIZE)]

    def add_query(self, l:int, r:int, i:int):
        """
        半開区間 [l,r)
        """
        sft=self.shift
        h=l*self.BSIZE//self.N
        self.data[i]=(l<<sft)|r
        self.query[h].append(((r if h&1 else -r)<<sft)+i)
    def solve(self):
        mask=(1<<self.shift)-1
        assert max(self.N, self.Q)<=mask
        L=R=0
        ret = [0]*self.Q
        for bucket in self.query:
            bucket.sort()
            for lri in bucket:
                i = lri&mask
                l,r=divmod(self.data[i],1<<self.shift)
                while L>l:
                    L-=1
                    self.add_left(L)
                    # print('add_left', l, r)
                while R<r:
                    self.add_right(R)
                    R+=1
                    # print('add_right', l, r)
                while L<l:
                    self.remove_left(L)
                    L+=1
                    # print('remove_left', l, r)
                while R>r:
                    R-=1
                    self.remove_right(R)
                    # print('remove_right', l, r)
                ret[i] = self.get_state()
        return ret

# N,Q=map(int,input().split())
N=int(input())
A=list(map(int,input().split()))
Q=int(input())
if len(set(A))==1:
    for i in range(Q):
        print(0)
    exit()


class Mo(_Mo):
    LINF = 0
    RINF = 10**10
    sm = SortedMultiset([LINF,RINF])
    def __init__(self, N, Q):
        super().__init__(N, Q)
        self.value = 0
    def get_state(self):
        return self.value
    # https://atcoder.jp/contests/abc293/tasks/abc293_g
    def add_left(self, i):
        a = A[i]
        l = Mo.sm.lt(a)
        r = Mo.sm.gt(l)
        if l != Mo.LINF:
            self.value += (l-a)**2
        if r != Mo.RINF:
            self.value += (r-a)**2
        if l != Mo.LINF and r!= Mo.RINF:
            self.value -= (l-r)**2
        Mo.sm.add(a)
    def remove_left(self, i):
        a = A[i]
        Mo.sm.discard(a)
        l = Mo.sm.lt(a)
        r = Mo.sm.gt(l)
        if l != Mo.LINF:
            self.value -= (l-a)**2
        if r != Mo.RINF:
            self.value -= (r-a)**2
        if l != Mo.LINF and r!= Mo.RINF:
            self.value += (l-r)**2

    add_right = add_left
    remove_right = remove_left



mo = Mo(N, Q)
for i in range(Q):
    l,r=map(int,input().split())
    mo.add_query(l-1,r, i)
ans = mo.solve()

print("\n".join(map(str,ans)))


#prefix#
# Lib_Mos_モアルゴリズム
#end#