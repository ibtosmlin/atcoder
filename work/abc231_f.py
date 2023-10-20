# https://atcoder.jp/contests/abc231/tasks/abc231_f
import sys; input: lambda _: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10001000); import pypyjit; pypyjit.set_param('max_unroll_recursion=-1')
int1=lambda x: int(x) - 1

# 部分和の計算と要素の更新の両方を効率的に行える
# 1-indexed
# sum(r)        :閉区間 [0,r] の合計を取得する
# [8] a0 + a1  + a2 + a3 + a4 + a5 + a6 + a7
# [4] a0 + a1  + a2 + a3
# [2] a0 + a1               [6] a4 + a5
# [1] a0       [3] a2       [5] a4        [7] a6

#                   [1000]
#           [0100]
#   [0010]                [0110]
# [0001]    [0011]      [0111]      [1111]
class BinaryIndexedTree:
    # 初期化処理
    def __init__(self, size):
        self.size = size
        self.dat = [0]*(size+1)
        self.depth = size.bit_length()

    def init(self, a):
        for i, x in enumerate(a):
            self.add(i, x)

    def add(self, i, x):
        i += 1
        while i <= self.size:
            self.dat[i] += x
            i += i & -i # 更新すべき位置

    def update(self, i, x):
        x -= self[i]
        self.add(i, x)

    def sum(self, r):
        """
        Returns
        -------
        sum of [0, r]
        """
        r += 1
        ret = 0
        while r>0:
            ret += self.dat[r]
            r -= r & -r # 加算すべき位置
        return ret

    def range_sum(self, l, r):
        """閉区間 [l,r] の合計を取得する

        Returns
        -------
        sum of [l, r]
        """
        if l == 0:
            return self.sum(r)
        else:
            return self.sum(r) - self.sum(l-1)


    def __getitem__(self, i):
        return self.range_sum(i, i)


    def right_bound_of_x(self, x):
        # pos       : sum([0, pos]) < x     となる最大のindex
        sum_, pos = 0, 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.dat[k] <= x:
                sum_ += self.dat[k]
                pos += 1 << i
        return pos

    def right_bound_include_x(self, x):
        # pos       : sum([0, pos]) <= x     となる最大のindex
        sum_, pos = 0, 0
        for i in range(self.depth, -1, -1):
            k = pos + (1 << i)
            if k <= self.size and sum_ + self.dat[k] < x:
                sum_ += self.dat[k]
                pos += 1 << i
        return pos

    def left_bound_of_x(self, x):
        # pos   : x < sum([0, pos])  となる最小のindex
        return self.right_bound_include_x(x) - 1

    def left_bound_include_x(self, x):
        # pos   : x <= sum([0, pos])  となる最小のindex
        return self.right_bound_of_x(x) - 1


#### for debug
    def _get_original_sequence(self):
        ret = [self[i] for i in range(self.size)]
        return ret

    def _get_aggrigate_sequence(self):
        return [self.sum(i) for i in range(self.size)]

    def __str__(self):
        seq = self._get_original_sequence()
        ret = 'original :' + ' '.join(map(str, seq))
        ret += '\n'
        seq = self._get_aggrigate_sequence()
        ret += 'aggrigate:' + ' '.join(map(str, seq))
        return ret

########################################
from collections import defaultdict

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

dics = {v:i for i, v in enumerate(sorted(set(B)))}
B = [dics[b] for b in B]

ps = defaultdict(list)
for ai, bi in zip(A, B):
    ps[ai].append(bi)

for v in ps.values():
    v.sort(reverse=True)

bit = BinaryIndexedTree(len(dics)+1)
ret = 0
cnt = 0
for a in sorted(set(A)):
    bs = ps[a]
    for b in bs:
        bit.add(b, 1)
        cnt += 1
    for b in bs:
        ret += cnt - bit.sum(b-1)
print(ret)
