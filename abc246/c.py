N,K,X=map(int, input().split())
array=list(map(int, input().split()))
rests=[]
ret=0
for a in array:
    q,r=divmod(a,X)
    if K>=q:
        rests.append(r)
        K-=q
    else:
        q-=K
        K=0
        ret+=q*X+r
rests.sort(reverse=True)
for i in range(K,len(rests)):
    ret+=rests[i]
print(ret)
