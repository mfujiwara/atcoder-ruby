N=int(input())
ret=0
for i in range(N):
    ret+=(1+i)*(N-i)
for _ in range(N-1):
    u,v=map(int, input().split())
    if u>v:
        u,v=v,u
    ret-=u*(N+1-v)
print(ret)
