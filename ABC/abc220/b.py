K=int(input())
A,B=map(int, input().split())
C=D=0
i=0
while A>0:
    A,r=divmod(A,10)
    C+=pow(K,i)*r
    i+=1
i=0
while B>0:
    B,r=divmod(B,10)
    D+=pow(K,i)*r
    i+=1
print(C*D)
