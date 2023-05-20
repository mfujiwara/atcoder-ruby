N,K=map(int, input().split())
rets0=[]
base=0
while base+4*K<=N:
    rets0+=[base+i+K for i in range(K)] + [base+i for i in range(K)]
    base+=2*K
N-=base
rets=[-1]*N
done=[False]*N
for k in range(K):
    if N-1-k-K<0:
        break
    rets[N-1-k-K]=N-1-k
    done[N-1-k]=True
for k in range(K):
    if rets[k]!=-1: break
    if done[k+K]:
        if rets[k]==k+K:
            break
        else:
            print(-1)
            exit()
    rets[k]=k+K
    done[k+K]=True
j=0
for i in range(N):
    if rets[i]==-1:
        while done[j]:
            j+=1
        if abs(i-j)<K:
            print(-1)
            exit()
        rets[i]=j
        done[j]=True
rets=[ret+base for ret in rets]
print(*[ret+1 for ret in rets0+rets])
