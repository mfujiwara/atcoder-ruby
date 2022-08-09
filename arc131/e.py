N=int(input())
total=N*(N-1)//2
target,r=divmod(total,3)
if r!=0:
    print("No")
    exit()
a,b,c=0,0,0
rets=[]
for i in range(N-1,0,-1):
    if a+i<=target:
        a+=i
        rets.append("R")
    elif b+i<=target:
        b+=i
        rets.append("B")
    elif c+i<=target:
        c+=i
        rets.append("W")
    else:
        print("No")
        exit()
    if a==target or b==target or c==target:
        break
print("Yes")
for i in range(N-1):
    if i<len(rets):
        print(rets[i]*(N-1-i))
    else:
        t=N-1-i
        ac,bc,cc=0,0,0
        if a<target:
            ac=min(target-a,t)
            a+=ac
            t-=ac
        if b<target:
            bc=min(target-b,t)
            b+=bc
            t-=bc
        if c<target:
            cc=min(target-c,t)
            c+=cc
            t-=cc
        print("R"*ac+"B"*bc+"W"*cc)
