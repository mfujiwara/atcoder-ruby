import collections
N,K=map(int, input().split())
array=list(map(int, input().split()))
indexes=collections.defaultdict(list)
for i,a in enumerate(array):
    indexes[a].append(i)
nexts=[-1]*N
for key in indexes:
    ind=indexes[key]
    for i,index in enumerate(ind):
        nexts[index]=ind[(i+1)%len(ind)]    
loop=1
cur=0
while cur!=N:
    if cur>=nexts[cur]:
        loop+=1
    cur=nexts[cur]+1
K%=loop
M=K*N
cur=0
while True:
    if cur>=nexts[cur]:
        diff=nexts[cur]-cur+N+1
    else:
        diff=nexts[cur]-cur+1
    if M<diff:
        break
    else:
        M-=diff
        cur=nexts[cur]+1
boxes=[0]*N*2
indexes=collections.defaultdict(lambda: 2*N)
start=cur
cur=0
for i in range(start,start+M):
    a=array[i%N]
    k=indexes[a]
    if k<cur and boxes[k]==a:
        cur=k
        indexes[a]=2*N
    else:
        boxes[cur]=a
        indexes[a]=cur
        cur+=1
print(*boxes[:cur])
