MOD=998244353
N=int(input())
mini=1
maxi=10
ret=0
while mini<=N:
    a=min(maxi-1,N)-mini+1
    a%=MOD
    ret+=(1+a)*(a)//2
    ret%=MOD
    mini*=10
    maxi*=10
print(ret)
