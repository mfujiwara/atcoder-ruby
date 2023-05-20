N=list(map(int,list("0"+input())))
N=N[::-1]
ret0=0
ret1=10
for n in N:
    ret0,ret1=min(ret0+n,ret1+1+n),min(ret0+10-n,ret1+9-n)
print(ret0)
