N,C=map(int, input().split())
array=list(map(int, input().split()))
rets=[0]*(C+1)
last=[-1]*(C+1)
for i,a in enumerate(array):
    diff=i-last[a]
    rets[a]+=(diff-1)*diff//2
    last[a]=i
all=(N+1)*N//2
for a in range(1,C+1):
    diff=N-last[a]
    rets[a]+=(diff-1)*diff//2
    print(all-rets[a])
