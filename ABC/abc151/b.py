N,K,M=map(int, input().split())
array=list(map(int, input().split()))
a=N*M-sum(array)
if a>K:
    print(-1)
else:
    print(max(0,a))
