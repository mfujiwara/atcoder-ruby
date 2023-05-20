H,W,X,Y=map(int, input().split())
X-=1
Y-=1
S=[input() for _ in range(H)]
ret=0
x=X
while x>=0 and S[x][Y]==".":
    ret+=1
    x-=1
x=X
while x<H and S[x][Y]==".":
    ret+=1
    x+=1
y=Y
while y>=0 and S[X][y]==".":
    ret+=1
    y-=1
y=Y
while y<W and S[X][y]==".":
    ret+=1
    y+=1
print(ret-3)
