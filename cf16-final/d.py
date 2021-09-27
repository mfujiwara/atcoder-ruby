N,M=map(int, input().split())
array=list(map(int, input().split()))
counts=[0]*100001
for a in array:
    counts[a]+=1
ret=0
mods=[0]*M
for i in range(100001):
    if counts[i]%2==1:
        counts[i]-=1
        tmod=(M-i%M)%M
        if mods[tmod]!=0:
            mods[tmod]-=1
            ret+=1
        else:
            mods[i%M]+=1
for i,c in enumerate(counts):
    if c==0: continue
    tmod=(M-i%M)%M
    if mods[tmod]>=c:
        mods[tmod]-=c
        ret+=c
    elif mods[tmod]>=2:
        ret+=mods[tmod]
        c-=mods[tmod]
        mods[tmod]=0
        ret+=c//2
    else:
        ret+=c//2
print(ret)
