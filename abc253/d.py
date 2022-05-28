import math
N,A,B=map(int, input().split())
ac=N//A
a=ac*(2*A+(ac-1)*A)//2
bc=N//B
b=bc*(2*B+(bc-1)*B)//2
C=A*B//math.gcd(A,B)
cc=N//C
c=cc*(2*C+(cc-1)*C)//2
ret=N*(1+N)//2-a-b+c
print(ret)
