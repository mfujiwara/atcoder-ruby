N=int(input())
abs=[]
for _ in range(N):
    a,b=map(int, input().split())
    abs.append((a,b))
c=0
for a,b in abs[::-1]:
    r=(a+c)%b
    if r!=0:
        c+=b-r
print(c)
