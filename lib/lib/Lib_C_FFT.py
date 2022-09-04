#name#
# 高速フーリエ変換(convolution, FFT)
#description#
#body#
# https://atcoder.jp/contests/atc001/tasks/fft_c
def convolve(a, b):
    def fft(f):
        d = n // 2
        v = w
        while d >= 1:
            u = 1
            for i in range(d):
                for j in range(i, n, 2*d):
                    f[j], f[j+d] = (f[j] + f[j+d]) % p, u * (f[j] - f[j+d]) % p
                u = u * v % p
            v = v * v % p
            d //= 2

    def ifft(f):
        d = 1
        while d < n:
            v = pow(invw, n // (2 * d), p)
            u = 1
            for i in range(d):
                for j in range(i, n, 2*d):
                    f[j+d] *= u
                    f[j], f[j+d] = (f[j] + f[j+d]) % p, (f[j] - f[j+d]) % p
                u = u * v % p
            d *= 2

    p, g = 1107296257, 5
    n0, n1 = len(a), len(b)
    n = 1 << (max(n0, n1) - 1).bit_length() + 1
    a = a + [0] * (n-n0)
    b = b + [0] * (n-n1)
    w = pow(g, (p - 1) // n, p)
    invw = pow(w, p-2, p)
    fft(a), fft(b)
    for i in range(n):
        a[i] = a[i] * b[i] % p
    ifft(a)
    invn = pow(n, p - 2, p)
    return [a[i] * invn % p for i in range(n0 + n1 - 1)]

N = int(input())
A = []
B = []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

print(0)
for xi in convolve(A, B):
    print(xi)

#prefix#
# Lib_C_FFT
#end#