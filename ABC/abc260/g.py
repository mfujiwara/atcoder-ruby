import collections
N,M=map(int, input().split())
S=[input() for _ in range(N)]
sss=[[0]*N for _ in range(N)]
sums=[[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        sss[i][j]=0 if S[i][j]=="X" else 1
        sums[i][j]=sss[i][j]
        if i>0:
            sums[i][j]+=sums[i-1][j]
        if j>0:
            sums[i][j]+=sums[i][j-1]
        if i>0 and j>0:
            sums[i][j]-=sums[i-1][j-1]
#print(sss,"sss")
#print(sums,"sums")
# 1行飛ばしの台形の累積
trap_sums=[[0]*(N*8) for _ in range(N)]
for i in range(N):
    for j in range(-i*2,N):
        if j>=0:
            trap_sums[i][j]=sss[i][j]
        trap_sums[i][j]+=trap_sums[i][j-2]
        if i>0:
            trap_sums[i][j]+=trap_sums[i-1][j+2]
            trap_sums[i][j]-=trap_sums[i-1][j]
#print(trap_sums,"trap_sums")
Q=int(input())
for _ in range(Q):
    x,y=map(int, input().split())
    x-=1
    y-=1
    # 基準の値
    ret=sums[x][y]
    # 台形を引く
    ret-=trap_sums[x][y-M*2]
    ret-=trap_sums[x][y-M*2-1]
    if x-M>=0:
        # 台形を足す
        ret+=trap_sums[x-M][y]
        ret+=trap_sums[x-M][y-1]
        # 長方形を引く
        ret-=sums[x-M][y]
    print(ret)
