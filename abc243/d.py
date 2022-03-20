N,X=map(int, input().split())
S=input()
s=[]
for ch in S:
    if ch=="U":
        if len(s)>0 and s[-1]!=0:
            s.pop()
        else:
            s.append(0)
    elif ch=="L":
        s.append(1)
    else:
        s.append(2)
for c in s:
    if c==0:
        X=X>>1
    elif c==1:
        X=X<<1
    else:
        X=(X<<1)+1
print(X)
