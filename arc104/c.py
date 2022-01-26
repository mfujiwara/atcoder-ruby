import collections
N=int(input())
AB=collections.defaultdict(lambda: (-1,-1))
C=[-1]*2*N
for _ in range(N):
    a,b=map(int, input().split())
    if a!=-1 and b!=-1:
        if a>=b:
            print("No")
            exit()
        c=b-a-1
        if a in AB or b in AB:
            print("No")
            exit()
        AB[a]=(1,b)
        AB[b]=(2,a)
        for i in range(a,b+1):
            if C[i-1]==-1:
                C[i-1]=c
            elif C[i-1]!=c:
                print("No")
                exit()
    elif a!=-1:
        if a in AB:
            print("No")
            exit()
        AB[a]=(1,-1)
    elif b!=-1:
        if b in AB:
            print("No")
            exit()
        AB[b]=(2,-1)
def calc(n,ccc):
    if n==2*N+1:
        print("Yes")
        exit()
    u,t=AB[n]
    c=ccc[n-1]
    if u!=-1 and t!=-1:
        calc(n+1,ccc)
    elif u==2:
        return
    elif c!=-1:
        if n+c+1>2*N:
            return
        preA=AB[n]
        preB=AB[n+c+1]
        if preA[0]!=-1 and preB[0]!=-1:
            return
        ddd=list(ccc)
        for i in range(n+1,n+c+2):
            if ccc[i-1] not in [-1,c]:
                return
            ddd[i-1]=c
        AB[n]=(1,n+c+1)
        AB[n+c+1]=(2,n)
        calc(n+1,tuple(ddd))
        AB[n]=preA
        AB[n+c+1]=preB
    else:
        for i in range(n+1,2*N+1):
            ddd=list(ccc)
            ddd[n-1]=i-n-1
            calc(n,tuple(ddd))
calc(1,tuple(C))
print("No")
