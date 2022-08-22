N,K=map(int, input().split())
array=list(map(int, input().split()))
if K==0:
    print(*array)
    exit()
def calc(array, k):
    rets=[(0,-1)]
    for a,c in array:
        while rets[-1][0]>a and (k>0 or rets[-1][1]==1):
            _,c1=rets.pop()
            k-=1-c1
        rets.append((a,c))
        k-=c
    while k>0:
        rets.pop()
        k-=1
    return [a for a,c in rets if c>=0]
array0=[(a,0) for a in array]
rets0=calc(array0,K)
#print(rets0)
mini=min(array[-K:])
mini_index=array.index(mini)
array1=[(a,1) for a in array[mini_index:]]+[(a,0) for a in array[:mini_index]]
rets1=calc(array1,K)
#print(rets1)
print(*min(rets0,rets1))
