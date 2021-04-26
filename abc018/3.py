R,C,K=map(int, input().split())
S1=[]
S2=[]
S3=[]
S4=[]
for _ in range(R):
    s=list(input())
    array=[K if s[i]=="x" else 0 for i in range(C)]
    S1.append(array[:])
    S2.append(array[:])
    S3.append(array[:])
    S4.append(array[:])
for i in range(R):
    for j in range(C):
        if S1[i][j]==K: continue
        a = S1[i-1][j] if i>0 else 0
        b = S1[i][j-1] if j>0 else 0
        S1[i][j]=max(a-1,b-1,0)
for i in range(R)[::-1]:
    for j in range(C):
        if S2[i][j]==K: continue
        a = S2[i+1][j] if i<R-1 else 0
        b = S2[i][j-1] if j>0 else 0
        S2[i][j]=max(a-1,b-1,0)
for i in range(R):
    for j in range(C)[::-1]:
        if S3[i][j]==K: continue
        a = S3[i-1][j] if i>0 else 0
        b = S3[i][j+1] if j<C-1 else 0
        S3[i][j]=max(a-1,b-1,0)
for i in range(R)[::-1]:
    for j in range(C)[::-1]:
        if S4[i][j]==K: continue
        a = S4[i+1][j] if i<R-1 else 0
        b = S4[i][j+1] if j<C-1 else 0
        S4[i][j]=max(a-1,b-1,0)
ret=0
for i in range(K-1,R-K+1):
    for j in range(K-1,C-K+1):
        if S1[i][j]==0 and S2[i][j]==0 and S3[i][j]==0 and S4[i][j]==0:
            ret+=1
print(ret)
