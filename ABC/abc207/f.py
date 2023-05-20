MOD=pow(10,9)+7
N=int(input())
edges=[[] for _ in range(N)]
for _ in range(N-1):
    u,v=map(int, input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)
targets=[0]
parents=[-1]*N
status=[0]*N
# dp0[i][j]:=頂点i以下のtreeで警備された頂点がj個（頂点iは警備されてない）
dp0=[[] for _ in range(N)]
# dp0[i][j]:=頂点i以下のtreeで警備された頂点がj個（頂点iは警備されていて、配置されてない）
dp1=[[] for _ in range(N)]
# dp0[i][j]:=頂点i以下のtreeで警備された頂点がj個（頂点iは警備されていて、配置されている）
dp2=[[] for _ in range(N)]
while targets:
    t=targets.pop()
    if status[t]==0:
        status[t]=1
        targets.append(t)
        for u in edges[t]:
            if status[u]==0:
                parents[u]=t
                targets.append(u)
    else:
        children=[]
        now0=[1,0]
        now1=[0,0]
        now2=[0,1]
        for u in edges[t]:
            if parents[t]==u: continue
            children.append(u)
        if len(children)==0:
            dp0[t]=now0
            dp1[t]=now1
            dp2[t]=now2
            continue
        for u in children:
            l=len(now0)+len(dp0[u])-1
            nexts0=[0]*l
            nexts1=[0]*l
            nexts2=[0]*l
            for i in range(len(now0)):
                for j in range(len(dp0[u])):
                    nexts0[i+j]+=now0[i]*dp0[u][j]%MOD
                    nexts0[i+j]%=MOD
                    nexts0[i+j]+=now0[i]*dp1[u][j]%MOD
                    nexts0[i+j]%=MOD
                    nexts1[i+j]+=now1[i]*dp0[u][j]%MOD
                    nexts1[i+j]%=MOD
                    nexts1[i+j]+=now1[i]*dp1[u][j]%MOD
                    nexts1[i+j]%=MOD
                    nexts1[i+j]+=now1[i]*dp2[u][j]%MOD
                    nexts1[i+j]%=MOD
                    nexts2[i+j]+=now2[i]*dp1[u][j]%MOD
                    nexts2[i+j]%=MOD
                    nexts2[i+j]+=now2[i]*dp2[u][j]%MOD
                    nexts2[i+j]%=MOD
                    if i+j+1==l: continue
                    nexts1[i+j+1]+=now0[i]*dp2[u][j]%MOD
                    nexts1[i+j+1]%=MOD
                    nexts2[i+j+1]+=now2[i]*dp0[u][j]%MOD
                    nexts2[i+j+1]%=MOD
            now0=nexts0
            now1=nexts1
            now2=nexts2
        dp0[t]=now0
        dp1[t]=now1
        dp2[t]=now2
for i in range(N+1):
    print((dp0[0][i]+dp1[0][i]+dp2[0][i])%MOD)
