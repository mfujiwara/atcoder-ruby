import bisect
N,K=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
a_array.sort()
b_array.sort()
left=a_array[0]*b_array[0]-1
right=a_array[-1]*b_array[-1]+1
while True:
    mid=(left+right)//2
    smaller=0
    same=0
    for a in a_array:
        k=mid//a
        ir=bisect.bisect_right(b_array,k)
        il=bisect.bisect_left(b_array,k)
        if ir>0 and b_array[ir-1]*a==mid:
            smaller+=il
            same+=ir-il
        else:
            smaller+=ir
    if smaller<K<=smaller+same:
        print(mid)
        exit()
    elif K<=smaller:
        right=mid
    else:
        left=mid
