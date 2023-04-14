N,K=map(int, input().split())
ret=1
while True:
    N//=K
    if N>0:
        ret+=1
    else:
        break
print(ret)
