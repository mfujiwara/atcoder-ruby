N=int(input())
p=sorted([int(input()) for _ in range(N)])
print(sum(p)-p[-1]//2)
