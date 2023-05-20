import bisect
INF=pow(10,9)+1
N,K=map(int, input().split())
array=list(map(int, input().split()))
mini=INF
v2i={}
vals=[]
for i in range(K-1,-1,-1):
    a=array[i]
    if a<mini:
        mini=a
        v2i[a]=i
        vals.append(a)
vals=vals[::-1]
ret=INF
for i in range(K,N):
    a=array[i]
    index=bisect.bisect_left(vals,a)
    if index>0:
        v=vals[index-1]
        ret=min(ret,i-K+K-v2i[v])
if ret==INF:
    print(-1)
else:
    print(ret)
