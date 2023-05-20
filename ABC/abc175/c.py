X,K,D=map(int, input().split())
k=abs(X)//D
X=abs(X)-D*min(K,k)
K-=min(K,k)
if K==0:
    print(X)
else:
    if K%2==0:
        print(X)
    else:
        print(abs(X-D))
