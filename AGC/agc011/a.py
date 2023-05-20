N,C,K=map(int, input().split())
ret=0
count=0
base_time=-1
ttt=[]
for _ in range(N):
    t=int(input())
    ttt.append(t)
for t in sorted(ttt):
    if base_time==-1:
        base_time=t
    if base_time+K<t:
        base_time=t
        ret+=1
        count=0
    count+=1
    if count==C:
        base_time=-1
        ret+=1
        count=0
if count>0:
    ret+=1
print(ret)
