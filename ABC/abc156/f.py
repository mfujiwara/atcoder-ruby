K,Q=map(int, input().split())
d_array=list(map(int, input().split()))
for _ in range(Q):
    N,X,M=map(int, input().split())
    q,r=divmod(N-1,K) # q周+r個
    total=0
    not_zero=0
    for i,d in enumerate(d_array):
        d%=M
        c=q+1 if i<r else q
        if d!=0:
            not_zero+=c
            total+=c*d
    start=X%M
    end=start+total
    box_count=end//M-start//M
    ret=not_zero-box_count
    print(ret)
