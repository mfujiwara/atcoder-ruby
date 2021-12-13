import collections
import itertools
N=int(input())
h_array=list(map(int, input().split()))
h_array=list(itertools.accumulate(h_array))
times=set()
mse=[]
for _ in range(N):
    m,s,e=map(int, input().split())
    mse.append((m,s,e))
    times.add(s)
    times.add(e)
times=sorted(list(times))
time2i={}
for i,t in enumerate(times):
    time2i[t]=i
edge_list=[]
stack=collections.defaultdict(list)
pres=collections.defaultdict(list)
mses=[[] for _ in range(len(times))]
dp=[0]*len(times)
for m,s,e in mse:
    s=time2i[s]
    e=time2i[e]
    mses[s].append((m,s,e))
for i,mse in enumerate(mses):
    if i>0:
        dp[i]=max(dp[i],dp[i-1])
    while stack[i]:
        stack_m,stack_s,stack_n=stack[i].pop()
        if len(pres[stack_m])<stack_n:
            pres[stack_m].append((stack_s))
        else:
            pres[stack_m][stack_n-1]=max(pres[stack_m][stack_n-1],stack_s)
    for m,s,e in mse:
        for i,pre_s in enumerate(pres[m]):
            dp[e]=max(dp[e],dp[pre_s]+h_array[i+1])
            stack[e].append((m,pre_s,i+2))
        dp[e]=max(dp[e],dp[s]+h_array[0])
        stack[e].append((m,s,1))
print(dp[-1])
