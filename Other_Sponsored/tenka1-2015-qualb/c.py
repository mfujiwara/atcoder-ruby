MOD=pow(10,9)+7
L=int(input())
ret=0
# x,x+1,y -> x+2<=y<2x+1 -> x-1
x=(L-1)//4
if x>=2:
    ret+=(x-1)*x//2%MOD

# x,x+1,y -> x+2<=y<=L-2x-1 -> L-3x-2
xs=(L-1)//4+1
xe=(L-3)//3
if xs<=xe:
    ret+=(L-3*xs-2+L-3*xe-2)*(xe-xs+1)//2%MOD

# y,x,x+1 -> 2<=y<=x-2 -> x-3
x=(L+1)//3
if x>=4:
    ret+=(x-2)*(x-3)//2%MOD

# y,x,x+1 -> 2<=y<=L-2x-1 -> L-2x-2
xs=(L+1)//3+1
xe=(L-3)//2
if xs<=xe:
    ret+=(L-2*xs-2+L-2*xe-2)*(xe-xs+1)//2%MOD

print(ret%MOD)
