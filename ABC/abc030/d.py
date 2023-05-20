N,a=map(int, input().split())
a-=1
k=int(input())
array=list(map(lambda e: int(e)-1, input().split()))
steps=[-1]*N
steps[a]=k
now=a
while k>0:
    nexts=array[now]
    if steps[nexts]>0 and k>steps[nexts]-steps[now]+1:
        k%=steps[nexts]-steps[now]+1
        steps[now]=k
        if k==0: break
    steps[nexts]=steps[now]-1
    k-=1
    now=nexts
print(now+1)
