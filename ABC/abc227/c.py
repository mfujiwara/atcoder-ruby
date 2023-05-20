N=int(input())
ret=0
for a in range(1,N+1):
    max_b=int(pow(N//a,0.5))
    if max_b<a:
        break
    for b in range(max_b,a-1,-1):
        max_c=N//a//b
        ret+=max(0,max_c-b+1)
print(ret)
