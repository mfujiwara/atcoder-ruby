K,A,B=map(int, input().split())
if A>=B-2:
    print(1+K)
else:
    if K<A+1:
        print(1+K)
    else:
        k=K-(A-1)
        q,r=divmod(k,2)
        print(A+q*(B-A)+r)
