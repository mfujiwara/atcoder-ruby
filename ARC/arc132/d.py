N,M=map(int,input().split())
S=list(map(int,input()))
T=list(map(int,input()))
# 0がi個の時の1の最大
max0=[0]*(N+1)
# 1がi個の時の0の最大
max1=[0]*(M+1)
ss=[0,0]
tt=[0,0]
for i in range(N+M):
    s=S[i]
    t=T[i]
    ss[s]+=1
    tt[t]+=1
    max0[ss[0]]=max(max0[ss[0]],ss[1])
    max0[tt[0]]=max(max0[tt[0]],tt[1])
    max1[ss[1]]=max(max1[ss[1]],ss[0])
    max1[tt[1]]=max(max1[tt[1]],tt[0])
#print(max0)
#print(max1)
# 最初に0に進む
d=[0,0]
ret0=0
while d!=[N,M]:
    v=max1[d[1]]
    if v>d[0]:
        ret0+=v-d[0]-1
        d[0]=v
    #print(d,ret0)
    v=max0[d[0]]
    if v>d[1]:
        ret0+=v-d[1]-1
        d[1]=v
    #print(d,ret0)
# 最初に1に進む
d=[0,0]
ret1=0
while d!=[N,M]:
    v=max0[d[0]]
    if v>d[1]:
        ret1+=v-d[1]-1
        d[1]=v
    #print(d,ret1)
    v=max1[d[1]]
    if v>d[0]:
        ret1+=v-d[0]-1
        d[0]=v
    #print(d,ret1)
print(max(ret0,ret1))
