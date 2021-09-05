H,W,K=map(int, input().split())
C=[]
for _ in range(H):
    c=[]
    for ch in input():
        if ch==".":
            c.append(0)
        else:
            c.append(1)
    C.append(c)
ret=0
for h_bit in range(1,2**H):
    hhh=[0]*H
    k=0
    while h_bit>0:
        h_bit,q=divmod(h_bit,2)
        if q==1:
            hhh[k]=1
        k+=1
    for w_bit in range(1,2**W):
        www=[0]*W
        k=0
        while w_bit>0:
            w_bit,q=divmod(w_bit,2)
            if q==1:
                www[k]=1
            k+=1
        total=0
        for i,hb in enumerate(hhh):
            for j,wb in enumerate(www):
                if hb==1 and wb==1 and C[i][j]==1:
                    total+=1
        if total==K:
            ret+=1
print(ret)
