import itertools
S=input()
K=int(input())
array=[]
for i,ch in enumerate(S):
    if ch=="Y":
        array.append(i-len(array))
sums=[0]+list(itertools.accumulate(array))
def check(m):
    for i in range(len(array)-m+1):
        target_index=(i+i+m-1)//2
        target=array[target_index]
        cost=0
        #1 i..target_index-1 
        if i<=target_index-1:
            cost+=target*(target_index-1-i+1)
            cost-=sums[target_index]-sums[i]
        #2 target_index+1..i+m-1
        if target_index+1<=i+m-1:
            cost+=sums[i+m]-sums[target_index+1]
            cost-=target*(i+m-1-(target_index+1)+1)
        if cost<=K:
            return True
    return False
if len(array)==0:
    print(0)
    exit()
ok=1
ng=len(array)+1
while ok+1!=ng:
    mid=(ok+ng)//2
    if check(mid):
        ok=mid
    else:
        ng=mid
print(ok)
