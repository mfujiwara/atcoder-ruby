R,G,B,N=map(int, input().split())
ret=0
for i in range(N//R+1):
    r=i*R
    for j in range(N//G+1):
        g=j*G
        b=N-r-g
        if b<0: break
        if b%B==0:
            ret+=1
print(ret)
