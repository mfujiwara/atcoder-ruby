M,K=map(int, input().split())
if K==0:
    rets=[]
    for i in range(pow(2,M)):
        rets.append(str(i))
        rets.append(str(i))
    print(" ".join(rets))
    exit()
if pow(2,M)<=K or (M==1 and K==1):
    print(-1)
    exit()
rets=[]
for i in range(pow(2,M)):
    if i==K: continue
    rets.append(str(i))
rets=rets+[str(K)]+rets[::-1]+[str(K)]
print(" ".join(rets))
