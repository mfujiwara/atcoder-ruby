N,M,D=map(int, input().split())
r_array=list(map(int, input().split()))
s_array=list(map(int, input().split()))
# ranges[i]:=左端の座標、右端の座標、得点の3つ組
ranges=[]
for i in range(M-1,0,-1):
    ranges.append((-r_array[i+1],-r_array[i],s_array[i]))
ranges.append((-r_array[1],r_array[1]+1,s_array[0]))
for i in range(1,M):
    ranges.append((r_array[i]+1,r_array[i+1]+1,s_array[i]))
start=-(N*D//2)
# memo[i]:=start+iを開始座標とした時の得点の差（累積和で得点そのもの）
memo=[0]*(D+1)
# 各rangeの貢献度に着目
for l,r,s in ranges:
    # l以上の矢があるかどうか
    if start+N*D<=l:
        # 最初は0、途中でも増えない
        memo[0]-=N*s
        memo[D]+=N*s
    elif start<=l-1:
        # 最初から1以上
        memo[0]-=(l-start+D)//D*s
        memo[(l-start)%D]+=s
        memo[D]+=(l-start)//D*s
    # r未満の矢があるかどうか
    if start+N*D<=r:
        # 最初はN、途中でも減らない
        memo[0]+=N*s
        memo[D]-=N*s
    elif start<=r-1:
        # 最初からN未満
        memo[0]+=(r-start+D)//D*s
        memo[(r-start)%D]-=s
        memo[D]-=(r-start)//D*s
ret=0
total=0
for v in memo:
    total+=v
    ret=max(ret,total)
print(ret)
