N=int(input())
array=list(map(int, input().split()))
ret=sum(array)
bits_total=[0]*30
for a in array:
    for i in range(30):
        a,r=divmod(a,2)
        if r==1:
            bits_total[i]+=1
for a in array:
    tmp=0
    base=1
    for i in range(30):
        a,r=divmod(a,2)
        if r==0:
            tmp+=bits_total[i]*base
        else:
            tmp+=(N-bits_total[i])*base
        base*=2
    ret=max(ret,tmp)
print(ret)
