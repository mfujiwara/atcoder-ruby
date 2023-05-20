import bisect
import itertools
INF=pow(10,9)
N=int(input())
array=list(map(int, input().split()))
sums=[0]+list(itertools.accumulate(array))
pre=[(INF,1)]*(N+1) # pre[i]:= arrayを[0,i)区間を分割したときのminmax
for i in range(2,N+1):
    v=bisect.bisect_right(sums,sums[i]//2)
    if abs(sums[i]-sums[v]*2)>abs(sums[i]-sums[v-1]*2):
        v-=1
    v=max(v,1)
    pre[i]=(sums[v],sums[i]-sums[v])
array=array[::-1]
sums=[0]+list(itertools.accumulate(array))
su=[(INF,1)]*(N+1) # pre[i]:= arrayを[0,i)区間を分割したときのminmax
for i in range(2,N+1):
    v=bisect.bisect_right(sums,sums[i]//2)
    if abs(sums[i]-sums[v]*2)>abs(sums[i]-sums[v-1]*2):
        v-=1
    v=max(v,1)
    su[i]=(sums[v],sums[i]-sums[v])
su=su[::-1]
ret=pow(10,9)
for i in range(2,N-1):
    a,b=pre[i]
    c,d=su[i]
    mini=min([a,b,c,d])
    maxi=max([a,b,c,d])
    ret=min(ret,maxi-mini)
print(ret)
