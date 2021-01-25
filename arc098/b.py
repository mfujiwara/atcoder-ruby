N=int(input())
array=list(map(int, input().split()))
ret=N
r=0
for i in range(N-1):
    if r==N-i:
        r-=1
        ret+=r
        continue
    if r>1:
        xor=xor^array[i-1]
        sum=xor
        r-=1
    else:
        r=0
        xor=array[i]
        sum=array[i]
    for j in range(1+r,N-i):
        xor2=xor^array[i+j]
        sum+=array[i+j]
        if xor2==sum:
            xor=xor2
            r+=1
        else:
            break
    ret+=r
print(ret)
