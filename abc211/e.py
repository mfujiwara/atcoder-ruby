N=int(input())
K=int(input())
MAP=[]
for _ in range(N):
    s=input()
    m=[]
    for ch in s:
        m.append(ch==".")
    MAP.append(m)
if K==1:
    ret=0
    for i in range(N):
        for j in range(N):
            if MAP[i][j]:
                ret+=1
    print(ret)
    exit()
comb1=((0,0),(0,1))
comb2=((0,0),(1,0))
combs=set()
combs.add(comb1)
combs.add(comb2)
for i in range(2,K):
    nexts=set()
    for comb in combs:
        for i,j in comb:
            for d1,d2 in [(-1,0),(1,0),(0,1),(0,-1)]:
                new_i=i+d1
                new_j=j+d2
                if (new_i,new_j) in comb:
                    continue
                if new_i<0 or  (new_i==0 and new_j<0):
                    continue
                new=list(comb)
                new.append((new_i,new_j))
                new.sort()
                nexts.add(tuple(new))                
    combs=nexts
ret=0
for i in range(N):
    for j in range(N):
        if not MAP[i][j]: continue
        for comb in combs:
            judge=True
            for x,y in comb:
                if 0<=i+x<N and 0<=j+y<N and MAP[i+x][j+y]:
                    continue
                else:
                    judge=False
                    break
            if judge:
                ret+=1
print(ret)
