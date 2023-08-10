# https://atcoder.jp/contests/abc313/tasks/abc313_d
n, k = map(int, input().split())
ret = [-1] * (n+1)
# まずk+1回やってa_1-a_k+1を決める
query = list(range(k+2))
xors = 0
for i in range(1, k+2):
    x = query[1:i] + query[i+1:]
    x = " ".join(map(str, x))
    print(f"? {x}", flush=True)
    ret[i] = int(input())
    xors ^= ret[i]
for i in range(1, k+2):
    ret[i] ^= xors

xors = 0
query = []
for i in range(k-1):
    xors ^= ret[i+1]
    query.append(i+1)

for i in range(k+2, n+1):
    x = query + [i]
    x = " ".join(map(str, x))
    print(f"? {x}", flush=True)
    ret[i] = int(input()) ^ xors

x = " ".join(map(str, ret[1:]))
print(f"! {x}", flush=True)


# https://atcoder.jp/contests/atc001/tasks/unionfind_a
