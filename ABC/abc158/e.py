N,P=map(int, input().split())
S=input()
if P==2:
    ret=0
    for i,ch in enumerate(S):
        if int(ch)%2==0:
            ret+=i+1
    print(ret)
    exit()
if P==5:
    ret=0
    for i,ch in enumerate(S):
        if int(ch)%5==0:
            ret+=i+1
    print(ret)
    exit()
S=list(map(int, list(S)))
ret=0
mods=[1]*N
for i in range(1,N):
    mods[i]=mods[i-1]*10%P
dp=[0]*P
t=0
for i in range(len(S)):
    t+=mods[i]*S[-1-i]%P
    t%=P
    if t==0:
        ret+=1
    ret+=dp[t]
    dp[t]+=1
print(ret)
