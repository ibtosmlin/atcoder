alps = 'abcdefghijklmnopqrstuvwxyz'
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar, Union, List
T = TypeVar('T')

class SortedSet(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
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
        return "SortedSet" + str(self.a)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

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

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
        return True

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
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        raise IndexError

    def _index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def _index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans

####################################
    def remove(self, x):
        if x in self:
            self.discard(x)

    def index(self, x):
        if x in self:
            return self._index(x)
        else:
            return None

    def strictly_left(self, x):
        return self.lt(x)

    def strictly_left_pos(self, x):
        v = self.lt(x)
        if v: return self.index(v)
        return None

    def strictly_right(self, x):
        return self.gt(x)

    def strictly_right_pos(self, x):
        v = self.gt(x)
        if v: return self.index(v)
        return None

########################################
n = int(input())
S = ['a'] + list(input()) + ['z']
inc = SortedSet()
pos = {si: SortedSet() for si in alps}

for i, si in enumerate(S):
    if i > 0:
        if S[i-1] > S[i]:
            inc.add(i)
    pos[si].add(i)

inc.add(2*n)
for si in alps:
    pos[si].add(-1)
    pos[si].add(n*2)

def update(x, c):
    if S[x-1] > c:
        inc.add(x-1)
    else:
        inc.remove(x-1)
    if c > S[x+1]:
        inc.add(x)
    else:
        inc.remove(x)
    pos[S[x]].remove(x)
    pos[c].add(x)
    S[x] = c


def isinc(l, r):
    return inc.ge(l) >= r

def iscontain(c, l, r):
    return pos[c].ge(0) >= l and pos[c].le(n+1) <= r

def check(l, r):
    if not isinc(l, r):
        return False
    cl = ord(S[l]) + 1
    rl = ord(S[r]) - 1
    if cl > rl:
        return True
    for ct in range(cl, rl+1):
        if not iscontain(chr(ct), l, r):
            return False
    return True




for _ in range(int(input())):
    que = input().split()
    if que[0] == '1':
        _, x, c = que
        x = int(x)
        update(x, c)
    else:
        _, l, r = que
        l, r = int(l), int(r)
        print('Yes' if check(l, r) else 'No')
