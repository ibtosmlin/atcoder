# https://atcoder.jp/contests/arc150/tasks/arc150_a
def check(n, k, s):
    onecount = 0
    zeros = [0]
    ones = [0]
    for i in range(n):
        if s[i] == '1':
            onecount += 1
        zeros.append(zeros[-1] + (s[i] == '0'))
        ones.append(ones[-1] + (s[i] == '1'))

    cnt = 0
    for i in range(n-k+1):
        if ones[i+k] == ones[i] + onecount and zeros[i+k]==zeros[i]:
            cnt += 1
    return cnt == 1



for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    print('Yes' if check(n, k, s) else 'No')
