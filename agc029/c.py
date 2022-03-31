N=int(input())
array=list(map(int, input().split()))
left=0
right=N+1
while left+1!=right:
    mid=(left+right)//2
    # 文字列のindexにcount種類目の文字がくる状態を考える
    # 基本はcount=0とする->最小なので省略して考えられる
    indexAndCount=[[-1,-1]] #番兵
    last=-1
    b=True
    for a in array:
        if a>last:
            # さらに長い文字数の場合はaを足すだけでいいので次に進む
            last=a
            continue
        last=a
        while indexAndCount[-1][0]>a:
            indexAndCount.pop()
        if indexAndCount[-1][0]!=a:
            # 先頭、もしくはaより小さい場合
            if mid==1:
                b=False
                break
            indexAndCount.append([a,1])
            continue
        # aと等しい場合
        while True:
            indexAndCount[-1][1]+=1
            if indexAndCount[-1][1]<mid:
                # midに収まっていればok
                break
            la,_=indexAndCount.pop()
            if indexAndCount[-1][0]!=la-1:
                # 1種類の文字だと繰り上げられないのでNG
                # 1文字目がmid種類目だと繰り上げられないのでNG
                if mid==1 or la==1:
                    b=False
                    break
                indexAndCount.append([la-1,1])
                break
        if not b:
            break
    if b:
        right=mid
    else:
        left=mid
print(right)
