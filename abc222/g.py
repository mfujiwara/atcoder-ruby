import math
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
    # Giant-step
    #R = pow(Z, M-2, M) # R = X^(-sq)
    R = pow(X,-sq,M)
    for i in range(1, sq+1):
        Y = Y * R % M
        if Y in D:
            return D[Y] + i*sq
    return -1
T=int(input())
for _ in range(T):
    K=int(input())
    if K%2==0:
        m=K//2*9
    else:
        m=K*9
    if math.gcd(10,m)!=1:
        print(-1)
        continue
    ret=babyStepGiantStep(10%m,1,m)
    print(ret)
