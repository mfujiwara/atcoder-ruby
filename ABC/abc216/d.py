import collections
N,M=map(int, input().split())
tubes=[]
for _ in range(M):
    k=int(input())
    array=list(map(int, input().split()))
    tubes.append(array)
stock=collections.defaultdict(list)
targets=[]
for i,array in enumerate(tubes):
    a=array.pop()
    stock[a].append(i)
    if len(stock[a])==2:
        targets.append(a)
while targets:
    t=targets.pop()
    for i in stock[t]:
        if len(tubes[i])==0: continue
        a=tubes[i].pop()
        stock[a].append(i)
        if len(stock[a])==2:
            targets.append(a)
for array in tubes:
    if len(array)>0:
        print("No")
        exit()
print("Yes")
