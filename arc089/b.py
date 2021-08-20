N,K=map(int, input().split())
K2=K*2
K4=K*4
black_memo=[[0]*K2 for _ in range(K2)]
white_memo=[[0]*K2 for _ in range(K2)]
for _ in range(N):
    x,y,c=input().split()
    x,y=int(x)%K2,int(y)%K2
    if c=="B":
        black_memo[x][y]+=1
    else:
        white_memo[x][y]+=1
black_sums=[[0]*K2 for _ in range(K2)]
white_sums=[[0]*K2 for _ in range(K2)]
for i in range(K2):
    for j in range(K2):
        b=black_memo[i][j]
        w=white_memo[i][j]
        if i>0:
            b+=black_sums[i-1][j]
            w+=white_sums[i-1][j]
        if j>0:
            b+=black_sums[i][j-1]
            w+=white_sums[i][j-1]
        if i>0 and j>0:
            b-=black_sums[i-1][j-1]
            w-=white_sums[i-1][j-1]
        black_sums[i][j]=b
        white_sums[i][j]=w
ret=0
for i in range(K2):
    for j in range(K2):
        def calc(sums,r,c):
            r,c=r%K2,c%K2
            ##
            w=sums[(r+K-1)%K2][(c+K-1)%K2]
            if r>K:
                w+=sums[K2-1][(c+K-1)%K2]
            if c>K:
                w+=sums[(r+K-1)%K2][K2-1]
            if r>K and c>K:
                w+=sums[K2-1][K2-1]
            ##
            if r>0:
                w-=sums[r-1][(c+K-1)%K2]
                if c>K:
                    w-=sums[r-1][K2-1]
            if c>0:
                w-=sums[(r+K-1)%K2][c-1]
                if r>K:
                    w-=sums[K2-1][c-1]
            ##
            if r>0 and c>0:
                w+=sums[r-1][c-1]            
            return w
        v=calc(black_sums,i,j)+calc(black_sums,i+K,j+K)+calc(white_sums,i,j+K)+calc(white_sums,i+K,j)
        ret=max(ret,v)
print(ret)
