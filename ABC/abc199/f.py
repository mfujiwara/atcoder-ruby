import collections
def mult(m1, m2):
    n=len(m1)
    ret=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j]+=m1[i][k]*m2[k][j]%MOD
            ret[i][j]%=MOD
    return ret
def ppow(m,n):
    if n==0:
        mm=[[1 if i==j else 0 for j in range(len(m))] for i in range(len(m))]
        return mm
    if n%2==0:
        return ppow(mult(m,m), n//2)
    else:
        return mult(ppow(mult(m,m), n//2),m)
MOD=pow(10,9)+7
N,M,K=map(int, input().split())
array=list(map(int, input().split()))
edges=collections.defaultdict(list)
for _ in range(M):
    x,y=map(int, input().split())
    x-=1
    y-=1
    edges[x].append(y)
    edges[y].append(x)
X=[[0]*N for _ in range(N)]
for i in range(N):
    X[i][i]=(2*M-len(edges[i]))
    X[i][i]*=pow(M*2,MOD-2,MOD)
    X[i][i]%=MOD
    for j in edges[i]:
        X[j][i]=pow(M*2,MOD-2,MOD)
XX=ppow(X,K)
for i in range(N):
    ret=0
    for j in range(N):
        ret+=array[j]*XX[j][i]%MOD
        ret%=MOD
    print(ret)
