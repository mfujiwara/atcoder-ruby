L=int(input())
n=1
edges=[]
while L>1:
    if L%2==1:
        edges.append(((n,-1,L-1)))
    L//=2
    edges.append((n,n+1,L))
    edges.append((n,n+1,0))
    n+=1
print(n,len(edges))
for u,v,c in edges:
    if v==-1:
        v=n
    print(u,v,c)
