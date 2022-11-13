N=int(input())
array=list(map(int, input().split()))
M=pow(10,6)
memo=[0]*M
for a in array:
    memo[a]+=1
for i in range(6):
    now=pow(10,i)
    for j in range(M):
        if (j//now)%10==9: continue # 9は繰り上がりしない
        memo[j+now]+=memo[j]
ret=0
d=0
for a in array:
    flg=1
    for j in range(6):
        now=pow(10,j)
        if (a//now)%10>=5:
            # 5以上は自分自身のペアが含まれるのでひく
            flg=0
    d+=flg
    ret+=memo[pow(10,6)-1-a] # 99999-a にある数が繰り上がり対象の数
print((ret-d)//2)
