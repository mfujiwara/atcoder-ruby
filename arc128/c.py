import itertools
N,M,S=map(int, input().split())
array=list(map(int, input().split()))
sums=[0]+list(itertools.accumulate(array))
ret=0
for i in range(N):
    for j in range(i,N+1):
        x2=M
        x1=(S-x2*(N-j))
        if i<j:
            x1/=(j-i)
        if x1<0 or x1>=M: continue
        r=x2*(sums[N]-sums[j])+x1*(sums[j]-sums[i])
        ret=max(ret,r)
print(ret)
