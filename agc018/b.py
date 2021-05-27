from collections import defaultdict
N,M=map(int, input().split())
A=[list(map(lambda e: int(e)-1, input().split())) for _ in range(N)]
left=0
right=N
while True: # O(log(N))
    if left+1==right:
        print(right)
        exit()
    mid=(left+right)//2
    open=[True]*M
    choice=[0]*N # i番目の人の選んでいる競技に順位
    enable=True
    while True: # O(N)
        indexes=defaultdict(list) # 競技 -> 人の一覧
        for i,c in enumerate(choice): # O(N)
            indexes[A[i][c]].append(i)
        overs=[] # 人の一覧
        for key in indexes: # O(M)
            idxs=indexes[key]
            if len(idxs)>mid:
                open[key]=False
                overs+=idxs
        if overs:
            for over in overs: # O(N)
                while choice[over]<M and not open[A[over][choice[over]]]:
                    choice[over]+=1
                if choice[over]==M:
                    enable=False
                    break
            if not enable:
                break
        else:
            break
    if enable:
        right=mid
    else:
        left=mid
