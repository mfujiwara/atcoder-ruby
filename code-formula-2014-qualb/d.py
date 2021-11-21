MOD=pow(10,9)+7
N=int(input())
ret=1
stack=1
rate=1
for i in range(N):
    a=int(input())
    v=stack+rate*a
    if v<rate*10+1 or i==N-1:
        ret*=v
        ret%=MOD
        stack=1
        rate=1
    else:
        rate*=10
        stack=v
print((MOD+ret-1)%MOD)
