import functools
def kaijou(a, b):
    return functools.reduce(lambda i, j: i*j, range(b,a+1), 1)
N=int(input())
dp=[0,0]
for n in range(2,N+1):
    total=3**n
    stay=0
    kitai=0
    for i in range(n+1):
        for j in range(n+1-i):
            k=n-i-j
            v1=kaijou(n,n-i+1)//kaijou(i,1) if i>0 else 1
            v2=kaijou(n-i,n-i-j+1)//kaijou(j,1) if j>0 else 1
            c=v1*v2
            x,y,z=sorted([i,j,k])
            if x==z or z==n:
                #print("stay",x,y,z)
                stay+=c
            else:
                t=x if x>0 else y
                #print("kitai",x,y,z,t)
                kitai+=(dp[t]+1)*c
    # dp[n]=kitai/total+dp[n]*stay/total + stay/total
    # dp[n]=(kitai+stay)/(toatl-stay)
    # x = 6/9 + 3*(x+1)/9
    dp.append((kitai+stay)/(total-stay))
print(dp[-1])
