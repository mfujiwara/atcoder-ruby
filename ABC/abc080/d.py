N,C=map(int, input().split())
counts=[[0 for i in range(C)] for j in range(10**5+2)]
max_t=0
for i in range(N):
    s,t,c=map(int, input().split())
    counts[s][c-1]+=1
    counts[t][c-1]-=1
    max_t=max(max_t,t)
ret=0
now=0
for i in range(max_t+1):
    count=counts[i]
    minus_count=0
    for cnt in count:
        if cnt<0:
            minus_count+=1
        elif cnt>0:
            now+=1
    ret=max(ret,now)
    now-=minus_count
print(ret)
