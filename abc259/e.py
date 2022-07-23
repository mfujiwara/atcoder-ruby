import collections
N=int(input())
pes=[collections.defaultdict(int) for _ in range(N)]
total=collections.defaultdict(int)
for i in range(N):
    m=int(input())
    for _ in range(m):
        p,e=map(int, input().split())
        pes[i][p]=e
        total[p]=max(total[p],e)
if N==1:
    print(1)
    exit()
max_count=collections.defaultdict(int)
for i in range(N):
    for p,e in pes[i].items():
        if total[p]==e:
            max_count[p]+=1
ret=1
for i in range(N):
    for p,e in pes[i].items():
        if total[p]==e and max_count[p]==1:
            ret+=1
            break
    #print("r",ret)
print(min(N,ret))
#print(max_count)