N=int(input())
ret=0
for _ in range(N):
    a,b=map(int, input().split())
    ret+=(a+b)*(b-a+1)//2
print(ret)
