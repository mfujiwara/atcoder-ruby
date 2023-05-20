import math
A,B,M=map(int, input().split())
def mult(m1, m2):
    n=len(m1)
    ret=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j]+=m1[i][k]*m2[k][j]%M
            ret[i][j]%=M
    return ret
def ppow(m,n):
    if n==0:
        mm=[[1 if i==j else 0 for j in range(len(m))] for i in range(len(m))]
        return mm
    if n%2==0:
        return ppow(mult(m,m), n//2)
    else:
        return mult(ppow(mult(m,m), n//2),m)
g=math.gcd(A,B)
if A<B:
    A,B=B,A
def calc(limit,e,base):
    X=[[e,0],[base,1]]
    X=ppow(X,limit)
    return X[1][0]    
# A mod M を求める
ret=calc(A,10,1)
# A*B/g mod M を求める
ret=calc(B//g,pow(10,g,M),ret)
print(ret)
