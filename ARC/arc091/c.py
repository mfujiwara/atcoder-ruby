N,A,B=map(int, input().split())
if A+B-1<=N<=A*B:
    rets=[]
    reverse=False
    for i in range((N+B-1)//B):
        if reverse:
            sub=[j for j in range(i*B+1,min((i+1)*B,N)+1)]
        else:
            sub=[j for j in range(min((i+1)*B,N),i*B,-1)]
            rest=N-len(rets)-B
            maxi=i+1+rest
            if maxi<A:
                diff=A-maxi
                head=sub[:B-diff-1]
                tail=sub[B-diff-1:]
                tail.sort()
                sub=head+tail
                reverse=True
        rets+=sub
    print(*rets)
else:
    print(-1)
