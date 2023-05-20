H,W=map(int, input().split())
S=[input() for _ in range(H)]
memo=[[None]*W for _ in range(H)]
def calc(i,j):
    if memo[i][j]!=None:
        return memo[i][j]
    nexts=[]
    if i<H-1 and S[i+1][j]!="#":
        nexts.append([i+1,j])
    if i<H-1 and j<W-1 and S[i+1][j+1]!="#":
        nexts.append([i+1,j+1])
    if j<W-1 and S[i][j+1]!="#":
        nexts.append([i,j+1])
    if len(nexts)==0:
        memo[i][j]=False
        return False
    for k,l in nexts:
        if not calc(k,l):
            memo[i][j]=True
            return True
    memo[i][j]=False
    return False
if calc(0,0):
    print("First")
else:
    print("Second")
