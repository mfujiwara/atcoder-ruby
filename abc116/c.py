N=int(input())
array=list(map(int, input().split()))
ret=0
while sum(array)>0:
    start=False
    for i,a in enumerate(array):
        if start and a==0:
            break
        if not start and a>0:
            start=True
        if start:
            array[i]-=1
    ret+=1
print(ret)
