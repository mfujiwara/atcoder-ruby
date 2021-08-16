K,S=map(int, input().split())
ret=0
for i in range(K+1):
    for j in range(K+1):
        k=S-i-j
        if 0<=k<=K:
            ret+=1
print(ret)
