N=int(input())
S=list(map(int, input().split()))
mins=[0,0,S[0]]
rets=[0,0,S[0]]
for i in range(1,N):
    diff=S[i]-S[i-1]
    v=rets[-3]+diff
    mins[(i-1)%3]=min(mins[(i-1)%3],v)
    rets.append(v)
if sum(mins)<0:
    print("No")
    exit()
diffs=[None,None,None]
lend=0
for i in range(3):
    if mins[i]<0:
        diffs[i]=-mins[i]
        lend-=mins[i]
for i in range(3):
    if diffs[i]==None:
        v=min(mins[i],lend)
        diffs[i]=-v
        lend-=v
for i in range(N+2):
    rets[i]+=diffs[i%3]
print("Yes")
print(*rets)
