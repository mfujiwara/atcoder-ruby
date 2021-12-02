MOD=pow(10,9)+7
N=int(input())
ret=1
for i in range(N):
    array=list(map(int, input().split()))
    ret*=sum(array)
    ret%=MOD
print(ret)
