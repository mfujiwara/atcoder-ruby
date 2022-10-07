T=int(input())
for _ in range(T):
    P,A,B,S,G=map(int, input().split())
    if S==G:
        print(0)
        continue
    if A==0:
        if B==G:
            print(1)
        else:
            print(-1)
        continue

    invA=pow(A,-1,P)
    invB=(-B)*invA%P
    bigA=1
    bigB=0
    m=int(P**0.5)
    
    small=dict()
    crr=G
    for i in range(m):
        if crr not in small:
            small[crr]=i
        crr=(invA*crr+invB)%P
        bigA=(bigA*A)%P
        bigB=(bigB*A+B)%P
    
    crr=S
    b=True
    for i in range(P//m+1):
        if crr in small:
            print(i*m+small[crr])
            b=False
            break
        crr=(bigA*crr+bigB)%P
    if b:
        print(-1)
