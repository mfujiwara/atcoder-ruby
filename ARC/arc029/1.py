N=int(input())
t=[]
if N==1:
    print(int(input()))
elif N==2:
    for _ in range(N):
        t.append(int(input()))
    print(max(t))
elif N==3:
    for _ in range(N):
        t.append(int(input()))
    ret=sum(t)
    ret=min(ret,max(t[0],t[1]+t[2]))
    ret=min(ret,max(t[1],t[0]+t[2]))
    ret=min(ret,max(t[2],t[1]+t[0]))
    print(ret)
else:
    for _ in range(N):
        t.append(int(input()))
    ret=sum(t)
    ret=min(ret,max(t[0],t[1]+t[2]+t[3]))
    ret=min(ret,max(t[1],t[0]+t[2]+t[3]))
    ret=min(ret,max(t[2],t[1]+t[0]+t[3]))
    ret=min(ret,max(t[3],t[1]+t[2]+t[0]))
    ret=min(ret,max(t[0]+t[1],t[2]+t[3]))
    ret=min(ret,max(t[0]+t[2],t[1]+t[3]))
    ret=min(ret,max(t[0]+t[3],t[1]+t[2]))
    print(ret)

