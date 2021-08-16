MOD=pow(10,9)+7
N=int(input())
array=list(map(int, input().split()))
if array[0]!=0:
    print(0)
    exit()
counts=[0]*(max(array)+1)
for a in array:
    counts[a]+=1
if counts[0]!=1:
    print(0)
    exit()
ret=1
for i in range(1,len(counts)):
    if counts[i]==0:
        print(0)
        exit() 
    base=pow(2,counts[i-1],MOD)-1
    ret*=pow(base,counts[i],MOD)
    ret%=MOD
    base=counts[i]*(counts[i]-1)//2
    ret*=pow(2,base,MOD)
    ret%=MOD
print(ret)
