X,Y,Z=map(int, input().split())
if X<Y<Z<0:
    print(-X)
elif X<Y<0<Z:
    print(Z*2-X)
elif X<Z<Y<0:
    print(-1)
elif X<Z<0<Y:
    print(-X)
elif X<0<Y<Z:
    print(-X)
elif X<0<Z<Y:
    print(-X)
elif Y<X<Z<0:
    print(-X)
elif Y<X<0<Z:
    print(-X)
elif Y<Z<X<0:
    print(-X)
elif Y<Z<0<X:
    print(X)
elif Y<0<X<Z:
    print(X)
elif Y<0<Z<X:
    print(X)
elif Z<X<Y<0:
    print(-1)
elif Z<X<0<Y:
    print(-X)
elif Z<Y<X<0:
    print(-X)
elif Z<Y<0<X:
    print(X)
elif Z<0<X<Y:
    print(X)
elif Z<0<Y<X:
    print(X-Z*2)
elif 0<X<Y<Z:
    print(X)
elif 0<X<Z<Y:
    print(X)
elif 0<Y<X<Z:
    print(-1)
elif 0<Y<Z<X:
    print(-1)
elif 0<Z<X<Y:
    print(X)
elif 0<Z<Y<X:
    print(X)
