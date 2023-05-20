N=int(input())
array=list(map(int, input().split()))
counts=[0]*401
for a in array:
    counts[a+200]+=1
ret=0
for i in range(400):
    for j in range(i+1,401):
        r=counts[i]*counts[j]*(j-i)**2
        ret+=r
print(ret)
