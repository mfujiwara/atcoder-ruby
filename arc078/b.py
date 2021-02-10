from collections import defaultdict
N=int(input())
edges=defaultdict(list)
for i in range(N-1):
    a,b=map(int, input().split())
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
boards=[False]*N
boards[0]=True
boards[N-1]=True
fenec=[0]
sunuke=[N-1]
score=0
while len(fenec)!=0 or len(sunuke)!=0:
    next_fenec=[]
    for i in fenec:
        for j in edges[i]:
            if not boards[j]:
                next_fenec.append(j)
                boards[j]=True
                score+=1
    fenec=next_fenec
    next_sunuke=[]
    for i in sunuke:
        for j in edges[i]:
            if not boards[j]:
                next_sunuke.append(j)
                boards[j]=True
                score-=1
    sunuke=next_sunuke
print("Fennec" if score>0 else "Snuke")
