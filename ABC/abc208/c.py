N,K=map(int, input().split())
array=list(map(int, input().split()))
q,r=divmod(K,N)
rets=[q]*N
indexes=[]
for i,a in enumerate(array):
    indexes.append((a,i))
indexes=sorted(indexes)
for k in range(r):
    a,i=indexes[k]
    rets[i]+=1
for r in rets:
    print(r)
