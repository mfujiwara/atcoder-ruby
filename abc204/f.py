MOD=998244353
def mult(m1, m2):
    n=len(m1)
    ret=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret[i][j]+=m1[i][k]*m2[k][j]
            ret[i][j]%=MOD
    return ret
def ppow(m,n):
    if n==0:
        mm=[[1 if i==j else 0 for j in range(len(m))] for i in range(len(m))]
        return mm
    if n%2==0:
        return ppow(mult(m,m), n//2)
    else:
        return mult(ppow(mult(m,m), n//2),m)
H,W=map(int, input().split())
matrix=[[0]*pow(2,H) for _ in range(pow(2,H))]
for j in range(2**H):
    for h_bit in range(2**H):
        h_bits=[]
        j_bits=[]
        for k in range(H):
            h_bits.append(1 if h_bit&pow(2,k)!=0 else 0)
            j_bits.append(1 if j&pow(2,k)!=0 else 0)
        dpp=[0]*(H+1)
        dpp[0]=1
        for k in range(H):
            if j_bits[k]==1 and h_bits[k]==1:
                continue
            if j_bits[k]==1 and h_bits[k]==0:
                dpp[k+1]+=dpp[k]
            if j_bits[k]==0 and h_bits[k]==1:
                dpp[k+1]+=dpp[k]
            if j_bits[k]==0 and h_bits[k]==0:
                dpp[k+1]+=dpp[k]
                if k<H-1 and j_bits[k+1]==0 and h_bits[k+1]==0:
                    dpp[k+2]+=dpp[k]
        if dpp[-1]>0:
            matrix[j][h_bit]+=dpp[-1]
            matrix[j][h_bit]%=MOD
ret=ppow(matrix,W)
print(ret[0][0])
