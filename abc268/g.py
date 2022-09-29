import collections
MOD=998244353
N=int(input())
sss=[]
s_to_index={}
for i in range(N):
    s=input()
    sss.append(s)
    s_to_index[s]=i
sorted_sss=sorted(sss)
sss.append("")
s_to_index[""]=N
stack=[""]
edges=collections.defaultdict(list)
for s in sorted_sss:
    while len(stack[-1])>=len(s) or stack[-1]!=s[:len(stack[-1])]:
        stack.pop()
    edges[s_to_index[stack[-1]]].append(s_to_index[s])
    stack.append(s)
# 自分を含まない子供の数
counts=[0]*(N+1)
# 自分を含む親の数
counts2=[0]*(N+1)
targets=[N]
status=[0]*(N+1)
while targets:
    t=targets.pop()
    if status[t]==0:
        status[t]=1
        targets.append(t)
        for u in edges[t]:
            targets.append(u)
            counts2[u]+=counts2[t]+1
    else:
        for u in edges[t]:
            counts[t]+=counts[u]+1
inv2=MOD - (MOD // 2)
for i in range(N):
    print((N-counts[i]+counts2[i])*inv2%MOD)
# print(counts)
# print(counts2)
