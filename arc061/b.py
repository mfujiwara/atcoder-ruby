H,W,N=map(int, input().split())
matrix=set()
check=set()
for _ in range(N):
    a,b=map(int, input().split())
    a-=1
    b-=1
    matrix.add((a,b))
    for i in range(3):
        for j in range(3):
            if 0<=a+i-2<H-2 and 0<=b+j-2<W-2:
                check.add((a+i-2,b+j-2))
rets=[0]*10
rest=(H-2)*(W-2)
for r,c in check:
    cnt=0
    for i in range(3):
        if r+i>=H: continue
        for j in range(3):
            if c+j>=W: continue
            if (r+i,c+j) in matrix:
                cnt+=1
    rets[cnt]+=1
    rest-=1
rets[0]=rest
for ret in rets:
    print(ret)
