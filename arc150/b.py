T=int(input())
rets=[]
for _ in range(T):
    A,B=map(int, input().split())
    # K(A+X)=(B+Y)
    # r=B-A*q
    q,r=divmod(B,A)
    if r==0:
        print(0)
        rets.append(0)
        continue
    if q==0:
        print(A-r)
        rets.append(A-r)
        continue
    # K==q+1
    # (q+1)*A=B+Y -> A=r+Y
    ret=A-r
    # K=q..1
    for i in range(q):
        # K==q-i
        # (q-i)(A+X)==(B+Y) -> X*(q-i)-Y==r+iA
        X=(r+i*A+q-i-1)//(q-i)
        if X>ret:
            break
        Y=X*(q-i)-r-i*A
        ret=min(ret,X+Y)
    print(ret)
    rets.append(ret)
#print(rets)
