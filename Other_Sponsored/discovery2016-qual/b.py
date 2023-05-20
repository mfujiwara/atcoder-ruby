import collections
N=int(input())
array=list(map(int, input().split()))
dic=collections.defaultdict(list)
for i,a in enumerate(array):
    dic[a].append(i)
keys=sorted(list(dic.keys()))
ret=0
now=0
for key in keys:
    idxs=dic[key]
    for i in range(len(idxs)):
        if idxs[i]<now:
            idxs[i]+=N
    idxs.sort()
    now=idxs[-1]
    if now>=N:
        now-=N
        ret+=1
if now!=0:
    ret+=1
print(ret)
