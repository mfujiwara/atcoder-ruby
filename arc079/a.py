N,M=map(int, input().split())
counts=[0]*(N+1)
for _ in range(M):
    a,b=map(int, input().split())
    if a>b:
        a,b=b,a
    if a==1:
        counts[b]+=1
    if b==N:
        counts[a]+=1
    if counts[a]==2 or counts[b]==2:
        print("POSSIBLE")
        exit()
print("IMPOSSIBLE")
