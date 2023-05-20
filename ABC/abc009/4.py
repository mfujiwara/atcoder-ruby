K,M=map(int, input().split())
a_array=list(map(int, input().split()))
c_array=list(map(int, input().split()))
if M<=len(a_array):
    print(a_array[M-1])
    exit()
X=[[0]*K for _ in range(K)]
for i in range(K-1):
    X[i+1][i]=pow(2,33)-1
for i in range(K):
    X[-1-i][-1]=c_array[i]
def mult(m1, m2):
    n=len(m1)
    ret=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j]^=m1[i][k]&m2[k][j]
    return ret
def ppow(m,n):
    if n==0:
        mm=[[pow(2,33)-1 if i==j else 0 for j in range(len(m))] for i in range(len(m))]
        return mm
    if n%2==0:
        return ppow(mult(m,m), n//2)
    else:
        return mult(ppow(mult(m,m), n//2),m)
ccc=ppow(X,M-K)
a_mat=[[0]*K if i!=0 else a_array for i in range(K)]
rets=mult(a_mat,ccc)
print(rets[0][-1])
