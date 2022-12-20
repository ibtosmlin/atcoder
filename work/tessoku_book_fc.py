# https://atcoder.jp/contests/tessoku-book/tasks/tessoku_book_fc
n = int(input()) - 1
ret = [4] * 10
for i in range(10):
    if n >> i & 1:
        ret[i] = 7
print(''.join(map(str, ret[::-1])))