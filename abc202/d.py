kaijou=[1]*61
for i in range(1,61):
    kaijou[i]=kaijou[i-1]*i
A,B,K=map(int, input().split())
k=K
ret=""
ar=A
br=B
for i in range(A+B):
    if ar==0:
        ret+="b"
    elif br==0:
        ret+="a"
    else:
        #aとした場合の数
        t=kaijou[ar+br-1]//kaijou[br]//kaijou[ar-1]
        if k>t:
            ret+="b"
            k-=t
            br-=1
        else:
            ret+="a"
            ar-=1
print(ret)
