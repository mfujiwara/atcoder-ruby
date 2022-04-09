N=int(input())
T=input()
x=0
y=0
v=(1,0)
for ch in T:
    if ch=="S":
        x+=v[0]
        y+=v[1]
    else:
        v=(v[1],-v[0])
print(x,y)
