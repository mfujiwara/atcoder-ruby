N=int(input())
rets=[[-1]*(N-i-1) for i in range(N-1)]
for i in range(N-1):
    for j in range(i+1,N):
        k=j-i-1
        if rets[i][k]!=-1: continue
        v=1
        while True:
            if (i%pow(2,v))//pow(2,v-1)!=(j%pow(2,v))//pow(2,v-1):
                rets[i][k]=v
                break
            v+=1
for ret in rets:
    print(*ret)
