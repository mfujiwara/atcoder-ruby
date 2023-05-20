N=int(input())
array=[]
for _ in range(N):
    c=int(input())
    array.append(c)
counts=[0]*N
for i,a in enumerate(array):
    for b in array:
        if a%b==0:
            counts[i]+=1
ret=0
for i in range(N):
    count=counts[i]
    k=(count+1)//2
    ret+=k/count
print(ret)
