L1,R1,L2,R2=map(int, input().split())
wall=[0]*101
for i in range(L1,R1+1):
    wall[i]+=1
for i in range(L2,R2+1):
    wall[i]+=1
ret=len([i for i in wall if i==2])
print(max(ret-1,0))
