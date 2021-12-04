N=int(input())
ret=0
i=1
while i<=N:
    v=N//i
    maxi_i=N//v
    ret+=(maxi_i-i+1)*v
    i=maxi_i+1
print(ret)
