N,K=map(int, input().split())
array=[0]+list(map(int, input().split()))
array.sort()
c=1
ret=0
while K>0 and len(array)>1:
    a=array.pop()
    if (a-array[-1])*c<=K:
        ret+=(a+array[-1]+1)*(a-array[-1])*c//2
        K-=(a-array[-1])*c
        c+=1
    else:
        q,r=divmod(K,c)
        ret+=(a+a-q+1)*q*c//2
        ret+=(a-q)*r
        K=0
print(ret)
