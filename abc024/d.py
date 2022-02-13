MOD=pow(10,9)+7
A=int(input())
B=int(input())
C=int(input())
#x+yCx=A
#x+y+1Cy=B
#x+y+1Cx=C
#(x+y)!/x!y! = A
#A*(x+y+1) = B*(x+1)
#A*(x+y+1) = C*(y+1)
y=(B*C-A*B+MOD)%MOD * pow((A*B+A*C-B*C+MOD)%MOD,MOD-2,MOD) %MOD
x=B*(y+1)%MOD * pow(C,MOD-2,MOD) %MOD -1
print(x,y)
