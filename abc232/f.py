N,X,Y=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
dp=[0]*pow(2,N)
for bit in range(1,pow(2,N)):
    indexes=[]
    k=0
    t_bit=bit
    while t_bit>0:
        if t_bit%2!=0:
            indexes.append(k)
        t_bit//=2
        k+=1
    v=pow(10,20)
    for i,ind in enumerate(indexes):
        pre_bit=bit-pow(2,ind)
        cost=dp[pre_bit]+(ind-i)*Y+abs(a_array[ind]-b_array[len(indexes)-1])*X
        v=min(v,cost)
    dp[bit]=v
print(dp[-1])
