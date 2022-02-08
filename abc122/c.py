import itertools
N,Q=map(int, input().split())
S=input()
check=[0]*N
for i in range(1,N):
    if S[i-1:i+1]=="AC":
        check[i]=1
counts=[0]+list(itertools.accumulate(check))
for _ in range(Q):
    l,r=map(int, input().split())
    print(counts[r]-counts[l])
