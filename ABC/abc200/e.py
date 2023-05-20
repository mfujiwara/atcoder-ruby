import bisect
import itertools
N,K=map(int, input().split())
dp1=[1 if 1<=i<=N else 0 for i in range(3*N+1)]
sums1=list(itertools.accumulate(dp1))
dp2=[sums1[max(0,i-1)]-sums1[max(0,i-N-1)] for i in range(3*N+1)]
sums2=list(itertools.accumulate(dp2))
dp3=[sums2[max(0,i-1)]-sums2[max(0,i-N-1)] for i in range(3*N+1)]
sums3=list(itertools.accumulate(dp3))
ijk=bisect.bisect_left(sums3,K)
K-=sums3[ijk-1]
dp=[]
base=[]
for i in range(ijk-1):
    if i==0 or i>N or ijk-i<2:
        dp.append(0)
        base.append(0)
    elif 2<=ijk-i<=N+1:
        dp.append(ijk-i-1)
        base.append(0)
    elif N+2<=ijk-i<=2*N:
        dp.append(2*N+1-ijk+i)
        base.append(ijk-i-N-1)
    else:
        dp.append(0)
        base.append(0)
sums=list(itertools.accumulate(dp))
i=bisect.bisect_left(sums,K)
K-=sums[i-1]
j=max(K+base[i],ijk-i-N)
k=ijk-i-j
print(i,j,k)
