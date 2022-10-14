import math
def is_prime(n):
    if n == 1: return False
    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False
    return True
N=int(input())
rets=[[-1]*N for _ in range(N)]
if N%2==0:
    v=N*N
    for i in range(N//2):
        for j in range(N):
            rets[i][j]=v
            v-=2
    e=rets[N//2-1][0]
    s=1
    while is_prime(e+s):
        s+=2
    for i in range(N//2,N):
        for j in range(N):
            rets[i][j]=s
            s=(s+2)%(N*N)
    for ret in rets:
        print(*ret)
else:
    rets[N//2-1][N//2]=2
    rets[N//2][N//2-1]=8
    v=4
    for i in range(N//2+1):
        for j in range(N):
            if rets[i][j]!=-1: continue
            rets[i][j]=v
            v+=2
            if v ==8:
                v+=2
            if v>=N*N:
                break
    s=N*N
    while is_prime(rets[N//2-1][N//2+1]+s):
        s-=2
    rets[N//2][N//2]=7
    rets[N//2+1][N//2-1]=1
    for i in range(N//2,N):
        for j in range(N):
            if rets[i][j]!=-1: continue
            rets[i][j]=s
            s-=2
            if s==1:
                s=N*N
            elif s==7:
                s-=2
    for ret in rets:
        print(*ret)
