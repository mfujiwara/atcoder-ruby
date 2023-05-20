board=[[0]*19 for _ in range(19)]
black=0
white=0
for i in range(19):
    for j,ch in enumerate(input()):
        if ch=="o":
            board[i][j]=1
            black+=1
        elif ch=="x":
            board[i][j]=-1
            white+=1
if black!=white and black!=white+1:
    print("NO")
    exit()
def calc(x,y,dx,dy):
    nb=0
    nw=0
    while 0<=x<19 and 0<=y<19:
        if board[x][y]==1:
            if nw>=5:
                return False
            nb+=1
            nw=0
        elif board[x][y]==-1:
            if nb>=5:
                return False
            nb=0
            nw+=1
        else:
            if nw>=5 or nb>=5:
                return False
            nw=0
            nb=0
        x+=dx
        y+=dy
    if nb>=5 or nw>=5:
        return False
    return True
def judge():
    for i in range(19):
        if not calc(i,0,0,1):
            return False
        if not calc(0,i,1,0):
            return False
    for i in range(19*2-1):
        if not calc(max(0,18-i),max(i-18,0),1,1):
            return False
        if not calc(max(0,i-18),min(18,i),1,-1):
            return False
    return True
if black==0 and white==0:
    print("YES")
    exit()
if black==white:
    t=-1
else:
    t=1
for i in range(19):
    for j in range(19):
        if board[i][j]==t:
            board[i][j]=0
            if judge():
                print("YES")
                exit()
            board[i][j]=t
print("NO")
