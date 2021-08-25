import collections
import bisect
N=int(input())
boxes=collections.defaultdict(list)
for _ in range(N):
    w,h=map(int, input().split())
    boxes[w].append(h)
keys=sorted(list(boxes.keys()))
memo=[] # memo[i]:=i個の箱を入れられる一番小さいh
for w in keys:
    news={}
    for h in sorted(boxes[w]):
        index=bisect.bisect_left(memo,h)
        if index in news:
            news[index]=min(news[index],h)
        else:
            news[index]=h
    for i in news:
        if len(memo)==i:
            memo.append(news[i])
        else:
            memo[i]=news[i]
print(len(memo))
