INF=pow(10,12)
N=int(input())
xyp=[]
base_distances=[]
for _ in range(N):
    x,y,p=map(int, input().split())
    xyp.append((x,y,p))
    base_distances.append(min(abs(x),abs(y)))
x_distances=[[d for d in base_distances] for _ in range(pow(2,N))]
y_distances=[[d for d in base_distances] for _ in range(pow(2,N))]
for bit in range(pow(2,N)):
    x_dis=x_distances[bit]
    y_dis=y_distances[bit]
    i=0
    while bit:
        if bit&1:
            x0=xyp[i][0]
            y0=xyp[i][1]
            for j in range(N):
                x_dis[j]=min(x_dis[j],abs(x0-xyp[j][0]))
                y_dis[j]=min(y_dis[j],abs(y0-xyp[j][1]))
        bit>>=1
        i+=1
for i in range(N):
    p=xyp[i][2]
    for bit in range(pow(2,N)):
        x_distances[bit][i]*=p
        y_distances[bit][i]*=p
# print(x_distances)
# print(y_distances)
rets=[INF]*(N+1)
for xy_bit in range(pow(2,N)):
    count=bin(xy_bit).count('1')
    x_bit=xy_bit
    while True:
        #print(xy_bit,x_bit,y_bit)
        ret=0
        x_dis=x_distances[x_bit]
        y_dis=y_distances[xy_bit^x_bit]
        for i in range(N):
            ret+=min(x_dis[i],y_dis[i])#*xyp[i][2]
        if rets[count]>ret:
            rets[count]=ret
        if not x_bit: break
        x_bit=(x_bit-1)&xy_bit
for ret in rets:
    print(ret)
