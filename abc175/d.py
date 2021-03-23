N,K=map(int, input().split())
p_array=array=list(map(int, input().split()))
c_array=array=list(map(int, input().split()))
loops=[]
done=[False]*N
for i in range(N):
    if done[i]: continue
    done[i]=True
    loop=[c_array[i]]
    next_i=p_array[i]-1
    while next_i!=i:
        done[next_i]=True
        loop.append(c_array[next_i])
        next_i=p_array[next_i]-1
    loops.append(loop)
ret=-10**9
for loop in loops:
    sums=[0]
    for l in loop:
        sums.append(sums[-1]+l)
    for l in loop:
        sums.append(sums[-1]+l)
    for l in loop:
        sums.append(sums[-1]+l)
    if len(loop)<=K:
        if sums[len(loop)]<0:
            for i in range(len(loop)):
                ret=max(ret,max(sums[i+1:i+len(loop)+1])-sums[i])
        else:
            base=(K//len(loop)-1)*sums[len(loop)]
            d=K%len(loop)+len(loop)
            for i in range(len(loop)):
                ret=max(ret,base+max(sums[i+1:i+d+1])-sums[i])
    else:
        for i in range(len(loop)):
            ret=max(ret,max(sums[i+1:i+K+1])-sums[i])
print(ret)
