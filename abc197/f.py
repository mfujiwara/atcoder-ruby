import collections
N,M=map(int, input().split())
matrix=[[0]*N for _ in range(N)]
edges=collections.defaultdict(lambda: collections.defaultdict(list))
for _ in range(M):
    a,b,c=input().split()
    a=int(a)-1
    b=int(b)-1
    edges[a][c].append(b)
    edges[b][c].append(a)
    matrix[a][b]=1
    matrix[b][a]=1
done=set()
targets=[(0,N-1)]
c=1
while targets:
    nexts=[]
    ret=pow(10,10)
    for ts,tt in targets:
        if matrix[ts][tt]==1:
            ret=min(ret,c*2-1)
        for key_s in edges[ts]:
            for ut in edges[tt][key_s]:
                for us in edges[ts][key_s]:
                    if ut==us:
                        ret=min(ret,c*2)
                    if (us,ut) not in done:
                        done.add((us,ut))
                        nexts.append((us,ut))
    if ret!=pow(10,10):
        print(ret)
        exit()
    targets=nexts
    c+=1
print(-1)
