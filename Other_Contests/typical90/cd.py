MOD=pow(10,9)+7
L,R=map(int, input().split())
ret=0
for i in range(19):
    # pow(10,i)..pow(10,i+1)-1
    if pow(10,i+1)-1<L:
        continue
    if R<pow(10,i):
        break
    start=max(pow(10,i),L)
    end=min(pow(10,i+1)-1,R)
    v=((start+end)*(end-start+1)//2)%MOD
    v*=(i+1)
    v%=MOD
    ret+=v
    ret%=MOD
print(ret)
