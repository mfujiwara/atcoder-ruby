N,A,B=map(int, input().split())
if A<=B:
    print(max(0,N-A+1))
else:
    q,r=divmod(N,A)
    #print(q,r)
    if q==0:
        print(0)
    else:
        ret=(q-1)*B+min(r+1,B)
        print(ret)

