import collections
MOD=pow(10,9)+7
S=input()
L=len(S)
K=int(input())
edges=collections.defaultdict(list)
stack=[-1]
for i,ch in enumerate(S):
    if ch=="(":
        p=stack[-1]
        edges[p].append(i)
        stack.append(i)
    else:
        stack.pop()
targets=[-1]
status=collections.defaultdict(int)
ddpp=collections.defaultdict(lambda: collections.defaultdict(int))
while targets:
    t=targets.pop()
    if status[t]==0:
        status[t]=1
        targets.append(t)
        for u in edges[t]:
            targets.append(u)
    else:
        status[t]=2
        if t==-1:
            ret=1
            for u in edges[t]:
                v=0
                for key1,val1 in ddpp[u].items():
                    if -K<=key1<=K:
                        v+=val1
                ret*=v
                ret%=MOD
            print(ret)
        else:
            dp=collections.defaultdict(int)
            dp[0]=2
            if K>=2:
                dp[2]=1
                dp[-2]=1
            for u in edges[t]:
                nexts=collections.defaultdict(int)
                for key0,val0 in dp.items():
                    for key1,val1 in ddpp[u].items():
                        if -K<=key1<=K:
                            nexts[key0+key1]+=val0*val1%MOD
                            nexts[key0+key1]%=MOD
                dp=nexts
        ddpp[t]=dp
