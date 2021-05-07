N=int(input())
counts=[[0]*19 for _ in range(19)]
for _ in range(N):
    a=input().split(".")
    if len(a)==1:
        a=int(a[0])*10**9
    else:
        a=int(a[0]+a[1])*10**(9-len(a[1]))
    e2=0
    e5=0
    while a%2==0 and e2<18:
        e2+=1
        a//=2
    while a%5==0 and e5<18:
        e5+=1
        a//=5
    counts[e2][e5]+=1
ret=0
for i in range(19):
    for j in range(19):
        for k in range(18-i,19):
            for l in range(18-j,19):
                if i==k and j==l:
                    ret+=counts[i][j]*counts[k][l]
                    ret-=counts[i][j]
                else:
                    ret+=counts[i][j]*counts[k][l]
print(ret//2)
