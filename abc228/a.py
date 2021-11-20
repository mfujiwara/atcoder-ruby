S,T,X=map(int, input().split())
if T<S:
    T+=24
while X<S:
    X+=24
if S<=X<T:
    print("Yes")
else:
    print("No")
