N=int(input())
C=input()
s=0
t=N-1
ret=0
while True:
    while s<N and C[s]=="R":
        s+=1
    while t>=0 and C[t]=="W":
        t-=1
    if s<t:
        s+=1
        t-=1
        ret+=1
    else:
        break
print(ret)
