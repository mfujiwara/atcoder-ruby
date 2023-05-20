N=int(input())
vw=[(0,0)]
for _ in range(N):
    v,w=map(int, input().split())
    vw.append((v,w))
dp=[None for _ in range(min(pow(2,10),N+1))]
# 木の根側から半分ともう半分でそれぞれ計算、最後に全通り試す
# dp[i][j]:=頂点iとその祖先で重さjを作るときの最大の価値を頂点2^10まで求める
dp[0]=[0]*(pow(10,5)+1)
for i in range(1,min(pow(2,10),N+1)):
    v,w=vw[i]
    d=dp[i//2][:]
    for j in range(pow(10,5),w-1,-1):
        d[j]=max(d[j-w]+v,d[j])
    dp[i]=d
Q=int(input())
for _ in range(Q):
    v,l=map(int, input().split())
    # 頂点2^10から先の数
    cnt=max(v.bit_length()-10,0)
    # 頂点vから近いものを全通り試して行ったときの価値と重さ
    dv=[0]*(1<<cnt)
    dw=[0]*(1<<cnt)
    for i in range(cnt):
        vv,ww=vw[v]
        for j in range(1<<i):
            dv[j+(1<<i)]=dv[j]+vv
            dw[j+(1<<i)]=dw[j]+ww
        v//=2
    ret=0
    for vv,ww in zip(dv,dw):
        if ww<=l:
            ret=max(ret,dp[v][l-ww]+vv)
    print(ret)
