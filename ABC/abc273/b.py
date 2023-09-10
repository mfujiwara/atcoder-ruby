X,K=map(int, input().split())
for i in range(K):
    x=X%pow(10,i+1)
    x//=pow(10,i)
    if x>=5:
        X+=pow(10,i)*(10-x)
    else:
        X-=pow(10,i)*x
print(X)
