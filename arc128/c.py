import itertools
N,M,S=map(int, input().split())
array=list(map(int, input().split()))
ret=0
while S>0:
    sums=list(itertools.accumulate(array[::-1]))[::-1]
    maxi=(array[-1],len(array)-1)
    for i in range(2,len(array)+1):
        tmp=sums[-i]/i
        if tmp>maxi[0]:
            maxi=(tmp,len(array)-i)
    v,index=maxi
    heights=min(M*(len(array)-index),S)
    ret+=v*heights
    S-=heights
    array=array[:index]
print(ret)
