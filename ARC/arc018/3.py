import collections
N,M=map(int, input().split())
x0,a,p=map(int, input().split())
if a%p==0:
    x1=(x0+a)%p
    if x0>x1:
        print(2*(N-1))
    else:
        print(0)
    exit()
array=[]
X=[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        k=i*M+j
        if i==0 and j==0:
            X[0][0]=x0
        else:
            X[i][j]=(x0+a*k)%p
        array.append(X[i][j])
array.sort()
v2i={}
for i,a in enumerate(array):
    v2i[a]=i
to_from=collections.defaultdict(list)
ret=0
for i in range(N):
    for j in range(M):
        row=v2i[X[i][j]]//M
        to_from[row].append(j)
        ret+=abs(row-i)
for i in range(N):
    froms=sorted(to_from[i])
    for j in range(M):
        t=froms[j]
        ret+=abs(j-t)
print(ret)
