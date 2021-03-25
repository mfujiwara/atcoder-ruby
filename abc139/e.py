import sys
N=int(input())
T=[list(map(lambda e: int(e)-1, input().split())) for _ in range(N)]
pre_self=[[-1]*(N-1) for _ in range(N)]
for i in range(N):
    pre_self[i][0]=0
targets=[] # (i, j) :i<j
for i in range(N):
    j=T[i][0]
    if i < j and T[j][0]==i:
        targets.append((i,j))
days=[[-1]*(N-1) for _ in range(N)]
progress=[0]*N
c=0
ret=0
while targets:
    i,j=targets.pop()
    c+=1
    i_idx=progress[i]
    j_idx=progress[j]
    day=max(pre_self[i][i_idx],pre_self[j][j_idx])+1
    ret=max(ret,day)
    progress[i]+=1
    progress[j]+=1
    if i_idx<N-2:
        pre_self[i][i_idx+1]=day
        opnt=T[i][i_idx+1]
        opnt_idx=progress[opnt]
        if T[opnt][opnt_idx]==i:
            targets.append((i,opnt) if i<opnt else (opnt,i))
    if j_idx<N-2:
        pre_self[j][j_idx+1]=day
        opnt=T[j][j_idx+1]
        opnt_idx=progress[opnt]
        if T[opnt][opnt_idx]==j:
            targets.append((j,opnt) if j<opnt else (opnt,j))
if c==N*(N-1)//2:
    print(ret)
else:
    print(-1)
