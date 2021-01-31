N=int(input())
array=list(map(int, input().split())) 
e=1
sum=0
ret1=0
for a in array:
    if e==1 and sum+a<=0:
        ret1+=1-sum-a
        a=1-sum
    elif e==-1 and sum+a>=0:
        ret1+=sum+a+1
        a=-1-sum
    sum+=a
    e*=-1
e=-1
sum=0
ret2=0
for a in array:
    if e==1 and sum+a<=0:
        ret2+=1-sum-a
        a=1-sum
    elif e==-1 and sum+a>=0:
        ret2+=sum+a+1
        a=-1-sum
    sum+=a
    e*=-1
print(min(ret1,ret2))
