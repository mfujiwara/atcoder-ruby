L,R=map(int, input().split())
ret=0
rets=[]
done=[0]*(R-L)
for i in range(2,R-L):
    if done[i]==1: continue
    diff=1-done[i]
    d=i
    while d<R-L:
        done[d]+=diff
        d+=i
    mini=max(2,(L+i-1)//i)
    maxi=R//i
    if mini!=maxi:
        n=maxi-mini
        ret+=(n*(n+1)//2)*diff
        # for ii in range(mini,maxi):
        #     for jj in range(ii+1,maxi+1):
        #         rets.append((ii*i,jj*i))
        #         if ii*i==12 and jj*i==18:
        #             print(f"aaa: {i}")
        for j in range(mini,maxi):
            ret-=(maxi//j-1)*diff
            # for ii in range(maxi//j-1):
            #     rets.remove((j*i,j*i+j*(ii+1)*i))
    #print(f"ret: {ret}")
print(ret*2)
