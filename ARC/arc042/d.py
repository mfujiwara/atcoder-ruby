def babyStepGiantStep(X, Y, M):
    D = {}
    sq = int(M**.5)+1
    # Baby-step
    Z = 1
    for i in range(sq):
        Z = Z * X % M
        if Z not in D:
            D[Z] = i+1
    if Y in D:
        return D[Y]
    R = pow(Z, M-2, M)
    for i in range(1, sq+1):
        Y = Y * R % M
        if Y in D:
            return D[Y] + i*sq
    return -1
X,P,A,B=map(int, input().split())
if A+P-1<=B:
    print(1)
    exit()
if A==B:
    print(pow(X,A,P))
    exit()
A%=P-1
B%=P-1
ret=P-1
if B-A<=pow(2,24):
    r=pow(X,A,P)
    ret=r
    for i in range(A+1,B+1):
        r=r*X%P
        ret=min(ret,r)
    print(ret)
    exit()
for i in range(1,P):
    r=babyStepGiantStep(X,i,P)
    rr=r%P
    if i%100==0:
        print(i)
    if r==-1:
        continue
    if A<=rr<=B or rr<=A<B<=rr:
        print(i)
        exit()
