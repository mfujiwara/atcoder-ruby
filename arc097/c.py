N=int(input())
w_array=[0]*N
b_array=[0]*N
array=[]
for i in range(N*2):
    c,a=input().split()
    a=int(a)-1
    if c=="W":
        w_array[a]=i
    else:
        b_array[a]=i
    array.append((c,a))
# memo_w[k][i]:=先頭からk番目までにある番号i以下の白の個数
# memo_b[k][i]:=先頭からk番目までにある番号i以下の黒の個数
memo_w=[]
memo_b=[]
pre_w=[0]*(N+1)
pre_b=[0]*(N+1)
for i,ca in enumerate(array):
    c,a=ca
    if c=="W":
        memo_b.append(pre_b)
        nexts_w=[0]
        for j in range(N):
            if j>=a:
                nexts_w.append(pre_w[j+1]+1)
            else:
                nexts_w.append(pre_w[j+1])
        memo_w.append(nexts_w)
    else:
        memo_w.append(pre_w)
        nexts_b=[0]
        for j in range(N):
            if j>=a:
                nexts_b.append(pre_b[j+1]+1)
            else:
                nexts_b.append(pre_b[j+1])
        memo_b.append(nexts_b)
    pre_w=memo_w[-1]
    pre_b=memo_b[-1]
# print(memo_w)
# print(memo_b)
# dp[i]:=白をi個を先頭に詰めた時の最低移動数と移動済みindex一覧
dp=[0]
for i in range(N):
    c=dp[-1]
    index=w_array[i]
    changed=i-memo_w[index][i]
    needs=index+changed-i
    dp.append(c+needs)
#print(dp)
for j in range(N):
    nexts=[]
    # 黒を足す
    c=dp[0]
    index=b_array[j]
    changed=j-memo_b[index][j]
    needs=index+changed-j
    nexts.append(c+needs)
    for i in range(N):
        # 白を足す
        c=nexts[-1]
        index=w_array[i]
        changed=i+j+1-memo_w[index][i]-memo_b[index][j+1]
        needs=index+changed-i-j-1
        nexts.append(c+needs)
        # 黒を足す
        c=dp[i+1]
        index=b_array[j]
        changed=i+j+1-memo_w[index][i+1]-memo_b[index][j]
        needs=index+changed-i-j-1
        nexts[-1]=min(nexts[-1],c+needs)
    dp=nexts
    #print(dp,j)
print(dp[-1])
