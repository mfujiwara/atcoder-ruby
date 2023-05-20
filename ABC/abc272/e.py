N,M=map(int, input().split())
array=list(map(int, input().split()))
memo=[set() for _ in range(M)]
for i,a in enumerate(array):
    # 0<=a+(i+1)*(x+1)<=N
    mini=-a//(i+1)-1
    maxi=(N-a)//(i+1)-1
    for x in range(mini,maxi+1):
        if 0<=x<M:
            v=a+(i+1)*(x+1)
            memo[x].add(v)
for m in memo:
    for i in range(N+1):
        if i not in m:
            print(i)
            break
