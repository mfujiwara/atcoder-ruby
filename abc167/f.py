N=int(input())
memo1=[]
memo2=[]
for _ in range(N):
    S=input()
    m=[]
    for ch in S:
        if ch=="(":
            if len(m)==0 or m[-1]<0:
                m.append(1)
            else:
                m[-1]+=1
        else:
            if len(m)==0:
                m.append(-1)
            else:
                m[-1]-=1
                if m[-1]==0:
                    m.pop()
    if len(m)==0:continue
    if m[0]>0:
        memo1.append((0,m[0]))
    else:
        m.append(0)
        if m[1]+m[0]>=0:
            memo1.append((-m[0],m[1]))
        elif m[1]+m[0]<0:
            memo2.append((-m[0],m[1]))
memo1.sort(key=lambda e:e[0])
memo2.sort(key=lambda e:-e[1])
c=0
for l,r in memo1+memo2:
    if c<l:
        print("No")
        exit()
    else:
        c-=l
        c+=r
if c==0:
    print("Yes")
else:
    print("No")
