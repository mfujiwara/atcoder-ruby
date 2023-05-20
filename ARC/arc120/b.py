MOD=998244353
H,W=map(int, input().split())
S=[[0]*3 for _ in range(H+W-1)]
for i in range(H):
    s=list(input())
    for j,ch in enumerate(s):
        if ch=="R":
            S[i+j][0]+=1
        elif ch=="B":
            S[i+j][1]+=1
        else:
            S[i+j][2]+=1
ret=1
for i,j,k in S:
    if i>0 and j>0:
        print(0)
        exit()
    if i==0 and j==0:
        ret*=2
        ret%=MOD
print(ret)
