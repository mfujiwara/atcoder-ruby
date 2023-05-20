L=int(input())
memo=[0]*5 # 0,2,1,2,0
for i in range(L):
    nexts=[0]*5
    a=int(input())
    nexts[0]=memo[0]+a
    if a==0:
        nexts[1]=min(memo[:2])+2
    elif a%2==0:
        nexts[1]=min(memo[:2])
    else:
        nexts[1]=min(memo[:2])+1
    if a==0:
        nexts[2]=min(memo[:3])+1
    elif a%2==1:
        nexts[2]=min(memo[:3])
    else:
        nexts[2]=min(memo[:3])+1
    if a==0:
        nexts[3]=min(memo[:4])+2
    elif a%2==0:
        nexts[3]=min(memo[:4])
    else:
        nexts[3]=min(memo[:4])+1
    nexts[4]=min(memo)+a
    memo=nexts
print(min(memo))
