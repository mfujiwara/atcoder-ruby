H,W=map(int, input().split())
CHOCO=[list(map(int, input().split())) for _ in range(H)]
MEMO=[[None]*W for _ in range(H)]
MEMO[0][0]=CHOCO[0][0]
def cal(i,j,k,l):
  if i==0 and j==0 and MEMO[k][l] != None:
    return MEMO[k][l]
  if i!=0 and j!=0:
    return cal(0,0,k,l)-cal(0,0,i-1,l)-cal(0,0,k,j-1)+cal(0,0,i-1,j-1)
  if i!=0:
    return cal(0,0,k,l)-cal(0,0,i-1,l)
  if j!=0:
    return cal(0,0,k,l)-cal(0,0,k,j-1)
  e = 1 if (k+l)%2==0 else -1
  if k==0:
    MEMO[k][l]=cal(i,j,k,l-1)+CHOCO[k][l]*e
    return MEMO[k][l]
  if l==0:
    MEMO[k][l]=cal(i,j,k-1,l)+CHOCO[k][l]*e
    return MEMO[k][l]
  else:
    MEMO[k][l]=cal(i,j,k-1,l)+cal(i,j,k,l-1)-cal(i,j,k-1,l-1)+CHOCO[k][l]*e
    return MEMO[k][l]

ret=0
for i in range(H)[::-1]:
  for j in range(W)[::-1]:
    for k in range(i,H)[::-1]:
      for l in range(j,W)[::-1]:
        r = abs((k-i+1)*(l-j+1))
        if r<=ret:
          continue
        if cal(i,j,k,l)==0:
          ret=r
print(ret)
