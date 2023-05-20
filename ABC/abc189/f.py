N,M,K=map(int, input().split())
array=set(map(int, input().split()))
c=0
for i in range(1,N):
    if i in array:
        c+=1
        if c==M:
            print(-1)
            exit()
    else:
        c=0
# rets[i]:= iからスタートした時の期待値が
#           rets[i][0] + rets[i][1]*x0
rets=[[0]*2 for _ in range(N+M+1)]
for i in range(N-1,-1,-1):
    if rets[i+1][0]==0:
        rets[i][0]=1
    else:
        rets[i][0]=rets[i+1][0]
    rets[i][1]=rets[i+1][1]*M

    if i+M+1 in array:
        rets[i][1]-=1
    else:
        rets[i][0]-=rets[i+M+1][0]/M
        rets[i][1]-=rets[i+M+1][1]
    if i+1 in array:
        rets[i][1]+=1
    else:
        rets[i][0]+=rets[i+1][0]/M
        rets[i][1]+=rets[i+1][1]
    rets[i][1]/=M
# x0 = rets[0][0] + rets[0][1]*x0
ret=rets[0][0]/(1-rets[0][1])
print(ret)
#print(rets)
