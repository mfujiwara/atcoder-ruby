N,T=map(int, input().split())
diffs=[]
total=0
for _ in range(N):
    a,b=map(int, input().split())
    total+=a
    diffs.append(a-b)
diffs.sort()
ret=0
while total>T and diffs:
    diff=diffs.pop()
    total-=diff
    ret+=1
if total<=T:
    print(ret)
else:
    print(-1)
