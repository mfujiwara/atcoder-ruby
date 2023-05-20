H,W=map(int, input().split())
B=[list(map(int, input().split())) for _ in range(H)]
S=[[0]*W for _ in range(H)]
for i in range(H):
    for j in range(W):
        S[i][j]=B[i][j]
        if i>0:
            S[i][j]+=S[i-1][j]
        if j>0:
            S[i][j]+=S[i][j-1]
        if i>0 and j>0:
            S[i][j]-=S[i-1][j-1]
# Hmax[i][j]:=i行からj行以下までを使った時の長方形の最大値
Hmax=[[-pow(10,9)]*H for _ in range(H)]
for i in range(H):
    for j in range(i,H):
        mini=0
        for w in range(W):
            total=S[j][w]
            if i>0:
                total-=S[i-1][w]
            Hmax[i][j]=max(Hmax[i][j],total-mini)
            mini=min(mini,total)
        if j>i:
            Hmax[i][j]=max(Hmax[i][j],Hmax[i][j-1])
# Wmax[i][j]:=i列からj列以下までを使った時の長方形の最大値
Wmax=[[-pow(10,9)]*W for _ in range(W)]
for i in range(W):
    for j in range(i,W):
        mini=0
        for h in range(H):
            total=S[h][j]
            if i>0:
                total-=S[h][i-1]
            Wmax[i][j]=max(Wmax[i][j],total-mini)
            mini=min(mini,total)
        if j>i:
            Wmax[i][j]=max(Wmax[i][j],Wmax[i][j-1])
#print(Hmax)
#print(Wmax)
maxi=-pow(10,10)
for i in range(H-1):
    for j in range(i+1,H):
        maxi=max(maxi,Hmax[i][j-1]+Hmax[j][H-1])
    #print("h",i,maxi)
for i in range(W-1):
    for j in range(i+1,W):
        maxi=max(maxi,Wmax[i][j-1]+Wmax[j][W-1])
    #print("w",i,maxi)
print(maxi)
