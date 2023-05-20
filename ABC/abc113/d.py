MOD=10**9+7
H,W,K=map(int, input().split())
lines=[0]*(W-1)
nones=[0]*W
targets=[[0]]
while targets:
    t=targets.pop()
    if len(t)==W:
        for i in range(W-1):
            lines[i]+=t[i+1]
        t+=[0]
        for i in range(W):
            if t[i]==0 and t[i+1]==0:
                nones[i]+=1
    else:
        if t[-1]==1:
            targets.append(t+[0])
        else:
            targets.append(t+[0])
            targets.append(t+[1])
status=[0]*W
status[0]=1
for i in range(H):
    tmp=[0]*W
    for i in range(W):
        tmp[i]+=status[i]*nones[i]
        tmp[i]%=MOD
    for i in range(W-1):
        tmp[i]+=status[i+1]*lines[i]
        tmp[i]%=MOD
        tmp[i+1]+=status[i]*lines[i]
        tmp[i+1]%=MOD
    status=tmp
print(status[K-1])
