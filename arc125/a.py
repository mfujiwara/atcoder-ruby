import collections
N,M=map(int, input().split())
S=list(map(int, input().split()))
T=list(map(int, input().split()))
pre=S[0]
moved=False
ret=0
for i,b in enumerate(T):
    if pre==b:
        ret+=1
    else:
        if moved:
            ret+=2
        else:
            r=N
            for j,a in enumerate(S):
                if a!=S[0]:
                    r=min([r,j,N-j])
            if r==N:
                print(-1)
                exit()
            else:
                ret+=r+1
                moved=True
        pre=b
print(ret)
