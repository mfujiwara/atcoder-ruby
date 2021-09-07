import functools
N=int(input())
S=list(map(ord,list(input())))
@functools.lru_cache(maxsize=None)
def calc(s1,s2):
    dp=[[0]*(len(s2)+1) for _ in range(len(s1)+1)]
    dp[0][0]=1
    for j in range(N):
        for k1 in range(j,-1,-1):
            k2=j-k1
            if 0<=k1<=len(s1) and 0<=k2<=len(s2):
                if k1<len(s1) and S[j+N]==s1[k1]:
                    dp[k1+1][k2]+=dp[k1][k2]
                if k2<len(s2) and S[j+N]==s2[k2]:
                    dp[k1][k2+1]+=dp[k1][k2]
    return dp[-1][-1]
ret=0
for i in range(pow(2,N)):
    s1=[]
    s2=[]
    for j in range(N):
        i,r=divmod(i,2)
        if r==1:
            s1.append(S[j])
        else:
            s2.append(S[j])
    ret+=calc(tuple(s1[::-1]),tuple(s2[::-1]))
print(ret)
