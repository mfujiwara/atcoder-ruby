K=int(input())
r=0
for i in range(1,K+1):
    for j in range(1,K+1):
        k=K//i//j
        if k==0: break
        r+=k    
print(r)
