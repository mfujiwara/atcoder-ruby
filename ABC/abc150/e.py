MOD=pow(10,9)+7
N=int(input())
array=list(map(int, input().split()))
array.sort(reverse=True)
ret=0
for i,a in enumerate(array):
    ret+=a*(i+2)
    ret%=MOD
ret*=pow(4,N-1,MOD)
ret%=MOD
print(ret)
