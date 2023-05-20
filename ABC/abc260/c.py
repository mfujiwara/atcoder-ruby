import collections


N,X,Y=map(int, input().split())
red=collections.defaultdict(int)
blue=collections.defaultdict(int)
red[N]=1
for i in range(N,1,-1):
    n=red[i]
    red[i]=0
    red[i-1]+=n
    blue[i]+=n*X
    #print(red,blue)

    n=blue[i]
    blue[i]=0
    red[i-1]+=n
    blue[i-1]+=n*Y
    #print(red,blue)
print(blue[1])

