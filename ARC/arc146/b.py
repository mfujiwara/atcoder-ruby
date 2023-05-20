N,M,K=map(int, input().split())
array=list(map(int, input().split()))
counts=[0]*N
ret=0
for k in range(30,-1,-1):
    bit=pow(2,k)
    plused_counts=[0]*N
    diff_counts=[0]*N
    for i in range(N):
        a=array[i]
        if a&bit>0: continue
        diff_counts[i]=bit-(a&(bit-1))
        plused_counts[i]=counts[i]+diff_counts[i]
    total=sum(sorted(plused_counts)[:K])
    if total<=M:
        ret+=bit
        for i in range(N):
            array[i]+=diff_counts[i]
        counts=plused_counts
        #print(array,total,ret)
print(ret)
