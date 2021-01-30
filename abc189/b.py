import sys
N,X=map(int, input().split())
X*=100
for i in range(N):
    v,p=map(int, input().split())
    al=v*p
    X-=al
    if X<0:
        print(i+1)
        sys.exit()
print("-1")
