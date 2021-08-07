MOD=3
N=int(input())
c=input()
total=0
base=pow(2,N-1,3)
f=[0,0] # 3で割れる数
g=[0,1] # 3で割れなくなった数のmod3
for i in range(2,N):
    k=0
    while i%3==0:
        i//=3
        k+=1
    f.append(f[-1]+k)
    g.append((i%MOD)*g[-1]%MOD)
g[0]=1
for i in range(0,N):    
    k=f[N-1]-f[i]-f[N-1-i]
    l=g[N-1]*g[i]*g[N-1-i]%MOD
    if k==0:
        if c[i]=="W":
            total+=1*base*l
            total%=3
        elif c[i]=="R":
            total+=2*base*l
            total%=3
if total==0:
    print("B")
elif total==1:
    print("W")
else:
    print("R")
