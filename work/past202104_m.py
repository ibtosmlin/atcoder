# https://atcoder.jp/contests/past202104-open/tasks/past202104_m
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
def int1(x): return int(x)-1
from collections import defaultdict

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
        "sm[-1]も可能"
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
a = list(map(int, input().split()))
INF = 10**10

C = defaultdict(int)
ss = SortedSet([INF])
seginfo = [None] * (n+1)
for l, al in enumerate(a):
    C[al] += 1
    ss.add(l)
    seginfo[l] = (l+1, al)

ret = sum((v * (v-1) // 2 for v in C.values()))

def remove(l):
    r, x = seginfo[l]
    ch(x, -(r-l))
    ss.discard(l)


def add(l, r, x):
    seginfo[l] = (r, x)
    ch(x, r - l)
    ss.add(l)


def divide(m):
    if m in ss: return
    l = ss.le(m)
    r, x = seginfo[l]
    seginfo[l] = (m, x)
    seginfo[m] = (r, x)
    ss.add(m)


def ch(x, d):
    global ret, C
    c = C[x]
    C[x] += d
    ret += (c+d) * (c+d-1) // 2 - c*(c-1) // 2


def query(l, r, x):
    divide(l)
    divide(r)

    nl = ss.le(l)
    while nl < r:
        nr, _ = seginfo[nl]
        remove(nl)
        nl = nr
    add(l, r, x)
    print(ret)


q = int(input())
for _ in range(q):
    l, r, x = map(int, input().split())
    l -= 1
    query(l, r, x)
