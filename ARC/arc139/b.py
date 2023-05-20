INF=pow(10,20)
T=int(input())
for _ in range(T):
    N,A,B,X,Y,Z=map(int, input().split())
    Y,Z=min(Y,A*X),min(Z,B*X)
    #if Y/A>X/B:
    #  Y,Z,A,B=Z,Y,B,A
    if Y/A>Z/B:
        Y,Z,A,B=Z,Y,B,A
    ret=INF
    if N//A<A-1:
        # N//A回以上使ったらNを超えてしまう
        # Aが大きい場合はこっちにしたらTLEしない
        for a in range(N//A+1):
            cost=a*Y
            l=N-a*A
            cb=l//B
            cost+=cb*Z
            l-=cb*B
            cost+=l*X
            ret=min(ret,cost)
    else:
        # BをA回以上使っても効率が良くなることはない
        # Aが小さい場合はこっちにしたらTLEしない
        for b in range(A):
            cost=b*Z
            l=N-b*B
            ca=l//A
            cost+=ca*Y
            l-=ca*A
            cost+=l*X
            ret=min(ret,cost)
    print(ret)
