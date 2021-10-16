N=int(input())
array=list(map(int, input().split()))
counts=[0]*pow(10,5)
for a in array:
    counts[a]+=1
    if a<pow(10,5)-1:
        counts[a+1]+=1
    if a>0:
        counts[a-1]+=1
print(max(counts))
