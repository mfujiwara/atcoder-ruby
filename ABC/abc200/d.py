N=int(input())
array=list(map(int, input().split()))
dp=[None]*200
for idx,a in enumerate(array):
    if dp[0]!=None:
        a_id=[len(dp[0])+1]+dp[0]+[idx+1]
        b_id=[1,idx+1]
        print("Yes")
        print(" ".join(map(str,a_id)))
        print(" ".join(map(str,b_id)))
        exit()
    dd={}
    dd[a%200]=[idx+1]
    for i in range(200):
        if dp[i]!=None:
            idxs=dp[i][:]
            idxs.append(idx+1)
            dd[(i+a)%200]=idxs
    for i in dd:
        idxs=dd[i]
        if dp[i]==None:
            dp[i]=idxs
        else:
            a_id=[len(dp[i])]+dp[i]
            b_id=[len(idxs)]+idxs
            print("Yes")
            print(" ".join(map(str,a_id)))
            print(" ".join(map(str,b_id)))
            exit()
print("No")
