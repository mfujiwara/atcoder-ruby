N=int(input())
ret=0
for i in range(N):
    x=input()
    for j,ch in enumerate(x):
        if ch=="x":
            ret+=1
        elif ch=="o" and (i==0 or pre[j]!="o"):
            ret+=1
    pre=x 
print(ret)
