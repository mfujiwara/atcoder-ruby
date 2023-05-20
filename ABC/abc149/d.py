N,K=map(int, input().split())
R,S,P=map(int, input().split())
T=input()
ret=0
for i in range(K):
    dp=[]
    c=i
    while c<N:
        d=[0]*3
        if c<K:
            if T[c]=="r":
                d[2]=P
            elif T[c]=="s":
                d[0]=R
            else:
                d[1]=S
        else:
            if T[c]=="r":
                d[0]=max(dp[-1][1],dp[-1][2])
                d[1]=max(dp[-1][0],dp[-1][2])
                d[2]=max(dp[-1][0],dp[-1][1])+P
            elif T[c]=="s":
                d[0]=max(dp[-1][1],dp[-1][2])+R
                d[1]=max(dp[-1][0],dp[-1][2])
                d[2]=max(dp[-1][0],dp[-1][1])
            else:
                d[0]=max(dp[-1][1],dp[-1][2])
                d[1]=max(dp[-1][0],dp[-1][2])+S
                d[2]=max(dp[-1][0],dp[-1][1])
        dp.append(d)
        c+=K
    ret+=max(dp[-1])
print(ret)
