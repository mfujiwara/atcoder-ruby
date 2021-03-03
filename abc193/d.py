K=int(input())
S=map(int, list(input()[:-1]))
T=map(int, list(input()[:-1]))
cards=[K]*10
sss=[0]*10
ttt=[0]*10
for s in S:
    sss[s]+=1
    cards[s]-=1
for t in T:
    ttt[t]+=1
    cards[t]-=1
base_s=0
base_t=0
for i in range(1,10):
    base_s+=i*10**sss[i]
    base_t+=i*10**ttt[i]
count=0
for i in range(1,10):
    if cards[i]==0: continue
    score_s=base_s+i*(10**(sss[i]+1)-10**sss[i])
    for j in range(1,10):
        if cards[j]==0 or cards[j]==1 and i==j: continue
        score_t=base_t+j*(10**(ttt[j]+1)-10**ttt[j])
        if score_s>score_t:
            if i!=j:
                count+=cards[i]*cards[j]
            else:
                count+=cards[i]*(cards[i]-1)
print(count/((9*K-8)*(9*K-9)))
