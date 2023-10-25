n=int(input())
print(*[i for _, i in sorted([(sorted(list(input())), i+1) for i in range(n)])])