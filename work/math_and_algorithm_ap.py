mod = 10**9+7
n = int(input())
fibo = [1] * (n+1)
for i in range(3, n+1):
    fibo[i] = (fibo[i-1] + fibo[i-2]) % mod
print(fibo[n])