N=int(input())
array=list(map(int, input().split()))
Q=int(input())
# Mo's Algorithm
M=int(pow(N,0.5))+1
mo=[[] for _ in range(M)]
for i in range(Q):
    l,r=map(int, input().split())
    l-=1
    r-=1
    mo[l//M].append((r,l,i))
rets=[0]*Q
# M個の分割ごとに計算していく
for i in range(M):
    # colors[i]:=現在の区間に色iの人がいる偶奇
    colors=[0]*(N+1)
    l1,r1=0,-1
    cnt=0
    # rが小さい順に処理する
    for r2,l2,index in sorted(mo[i]):
        # rの現在位置を調整
        if r1<=r2:
            for r in range(r1+1,r2+1):
                if colors[array[r]]:
                    cnt+=1
                colors[array[r]]^=1
        else:
            for r in range(r1,r2,-1):
                colors[array[r]]^=1
                if colors[array[r]]:
                    cnt-=1
        # lの現在位置を調整
        if l1<=l2:
            for l in range(l1,l2):
                colors[array[l]]^=1
                if colors[array[l]]:
                    cnt-=1
        else:
            for l in range(l1-1,l2-1,-1):
                if colors[array[l]]:
                    cnt+=1
                colors[array[l]]^=1
        rets[index] = cnt
        l1,r1 = l2,r2
print(*rets, sep='\n')
