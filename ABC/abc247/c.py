N=int(input())
ret=[1]
for i in range(2,N+1):
    ret=ret+[i]+ret
print(*ret)
