# https://atcoder.jp/contests/math-and-algorithm/tasks/math_and_algorithm_r
from collections import defaultdict, Counter, deque
n = int(input())
a = list(map(int, input().split()))
CA = Counter(a)
ret = 0
ret += CA[100] * CA[400]
ret += CA[200] * CA[300]
print(ret)
