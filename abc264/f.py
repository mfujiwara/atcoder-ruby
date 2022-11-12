INF=pow(10,18)
H,W=map(int, input().split())
r_array=list(map(int, input().split())) # len(r_array)==H
c_array=list(map(int, input().split())) # len(c_array)==W
A=[list(map(int, list(input()))) for _ in range(H)]
rets=[]
#print(A)
for d in range(2):
    # iを移動する
    # dp[j][0]:=右向き 行変更なし
    # dp[j][1]:=右向き 行変更あり
    # dp[j][2]:=下向き 列変更なし
    # dp[j][3]:=下向き 列変更あり
    dp=[[INF]*4 for _ in range(W)]
    if A[0][0]==d:
        dp[0][0]=0
        dp[0][1]=r_array[0]+c_array[0]
        dp[0][2]=0
        dp[0][3]=r_array[0]+c_array[0]
    else:
        dp[0][0]=c_array[0]
        dp[0][1]=r_array[0]
        dp[0][2]=r_array[0]
        dp[0][3]=c_array[0]
    for i in range(H):
        nexts=[[INF]*4 for _ in range(W)]
        for j in range(W):
            if j+1<W:
                a=A[i][j+1]
                # from dp[0] dp[1]
                if a==d:
                    dp[j+1][0]=min(dp[j+1][0],dp[j][0])
                    dp[j+1][1]=min(dp[j+1][1],dp[j][1]+c_array[j+1])
                    dp[j+1][2]=min(dp[j+1][2],dp[j][0])
                    dp[j+1][3]=min(dp[j+1][3],dp[j][1]+c_array[j+1])
                else:
                    dp[j+1][0]=min(dp[j+1][0],dp[j][0]+c_array[j+1])
                    dp[j+1][1]=min(dp[j+1][1],dp[j][1])
                    dp[j+1][2]=min(dp[j+1][2],dp[j][1])
                    dp[j+1][3]=min(dp[j+1][3],dp[j][0]+c_array[j+1])
            if i+1<H:
                a=A[i+1][j]
                # from dp[2] dp[3]
                if a==d:
                    nexts[j][0]=min(nexts[j][0],dp[j][2])
                    nexts[j][1]=min(nexts[j][1],dp[j][3]+r_array[i+1])
                    nexts[j][2]=min(nexts[j][2],dp[j][2])
                    nexts[j][3]=min(nexts[j][3],dp[j][3]+r_array[i+1])
                else:
                    nexts[j][0]=min(nexts[j][0],dp[j][3])
                    nexts[j][1]=min(nexts[j][1],dp[j][2]+r_array[i+1])
                    nexts[j][2]=min(nexts[j][2],dp[j][2]+r_array[i+1])
                    nexts[j][3]=min(nexts[j][3],dp[j][3])
        #print(dp,nexts)
        if i==H-1:
            rets.append(min(dp[-1]))
        dp=nexts
print(min(rets))
#print(dp[0],dp[1],dp[2],dp[3])
