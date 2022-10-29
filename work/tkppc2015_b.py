n = int(input())
ans = []
for i in range(n):
	ans.append((int(input()), -i-1))
ans.sort(reverse=True)
print(-ans[0][1])
