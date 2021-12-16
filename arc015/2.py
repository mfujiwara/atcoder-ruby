N=int(input())
rets=[0]*6
for _ in range(N):
    M,m=map(float, input().split())
    if M>=35:
        rets[0]+=1
    elif 30<=M<35:
        rets[1]+=1
    elif 25<=M<30:
        rets[2]+=1
    if m>=25:
        rets[3]+=1
    if m<0 and M>=0:
        rets[4]+=1
    if M<0:
        rets[5]+=1
print(*rets)
