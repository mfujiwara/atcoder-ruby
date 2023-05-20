import functools
S=input()
K=int(input())
dp=[[[0]*31 for _ in range(31)] for _ in range(31)]
dp[0][0][0]=1
for i in range(31):
    for j in range(31):
        for k in range(31):
            if i==j==k==0: continue
            if i>0:
               dp[i][j][k]+=dp[i-1][j][k]
            if j>0:
               dp[i][j][k]+=dp[i][j-1][k]
            if k>0:
               dp[i][j][k]+=dp[i][j][k-1]
counts=[0]*3
sss=[]
for ch in S:
    if ch=="K":
        counts[0]+=1
        sss.append(0)
    elif ch=="E":
        counts[1]+=1
        sss.append(1)
    else:
        counts[2]+=1
        sss.append(2)
@functools.lru_cache(maxsize=None)
def calc(s,counts,k):
    if k>=(len(s)-1)*len(s)//2:
        return dp[counts[0]][counts[1]][counts[2]]
    if k==0:
        return 1
    if len(s)==0:
        return 1
    ret=0
    for i in range(3):
        if counts[i]!=0:
            ind=s.index(i)
            if k>=ind:
                s2=list(s)
                s2.pop(ind)
                counts2=list(counts)
                counts2[i]-=1
                ret+=calc(tuple(s2),tuple(counts2),k-ind)
    return ret
ret=calc(tuple(sss),tuple(counts),K)
print(ret)
