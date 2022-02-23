import collections
MOD=998244353
X=int(input())
# 3>1*2
# 4=2*2
# 5<2*3
counts=collections.defaultdict(int)
counts[X]=1
queue=collections.deque([X])
while queue:
    x=queue.pop()
    if x<=4:
        break
    if x%2==0:
        y=x//2
        counts[y]+=counts[x]*2
        if len(queue)==0 or queue[0]!=y:
            queue.appendleft(y)
    else:
        y1=x//2
        y2=(x+1)//2
        counts[y1]+=counts[x]
        counts[y2]+=counts[x]
        if len(queue)==0 or queue[0]!=y2:
            queue.appendleft(y2)
        queue.appendleft(y1)
ret=1
for i in [2,3,4]:
    ret*=pow(i,counts[i],MOD)
    ret%=MOD
print(ret)
