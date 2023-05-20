N=int(input())
def move(u):
    baes_r,base_c=u[0]
    for i in range(len(u)):
        r,c=u[i]
        u[i]=(r-baes_r,c-base_c)
    return u
def rotate(u):
    for i in range(len(u)):
        r,c=u[i]
        u[i]=(-c,r)
    return u
s=[]
for i in range(N):
    for j,ch in enumerate(input()):
        if ch=="#":
            s.append((i,j))
s.sort()
s=move(s)
t=[]
for i in range(N):
    for j,ch in enumerate(input()):
        if ch=="#":
            t.append((i,j))
t.sort()
t=move(t)
if s==t:
    print("Yes")
    exit()
for i in range(3):
    s=rotate(s)
    s.sort()
    s=move(s)
    if s==t:
        print("Yes")
        exit()
print("No")
