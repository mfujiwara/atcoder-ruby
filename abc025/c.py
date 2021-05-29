B=[list(map(int, input().split())) for _ in range(2)]
C=[list(map(int, input().split())) for _ in range(3)]
scores={}
def calc(board,depth):
    key=int("".join(map(str,list(board))))
    if key in scores:
        return scores[key]
    if depth==9:
        s1,s2=0,0
        for i in range(2):
            for j in range(3):
                if board[i*3+j]==board[i*3+j+3]:
                    s1+=B[i][j]
                else:
                    s2+=B[i][j]
        for i in range(3):
            for j in range(2):
                if board[i*3+j]==board[i*3+j+1]:
                    s1+=C[i][j]
                else:
                    s2+=C[i][j]
        return (s1,s2)
    turn=(depth%2==0)
    ret=(-1,-1)
    for i,b in enumerate(board):
        if b==0:
            board[i]= 1 if turn else 2
            r=calc(board,depth+1)
            board[i]=0
            if turn:
                if ret[0]<r[0]:
                    ret=r
            else:
                if ret[1]<r[1]:
                    ret=r
    scores[key]=ret
    return ret
s1,s2=calc([0]*9,0)
print(s1)
print(s2)
