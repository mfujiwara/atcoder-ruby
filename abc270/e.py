import heapq
N,K=map(int, input().split())
array=list(map(int, input().split()))
array_with_index=[(a,i) for i,a in enumerate(array)]
heapq.heapify(array_with_index)
total=0
while K>0:
    a,i=array_with_index[0]
    a-=total
    if K>=a*len(array_with_index):
        K-=a*len(array_with_index)
        total+=a
        heapq.heappop(array_with_index)
        if K==0:
            for i in range(N):
                array[i]=max(0,array[i]-total)
            print(*array)
            exit()
    else:
        b=K//len(array_with_index)
        K-=b*len(array_with_index)
        total+=b
        for i in range(N):
            array[i]=max(0,array[i]-total)
        j=0
        while K>0:
            if array[j]>0:
                array[j]-=1
                K-=1
            j=(j+1)%N
        print(*array)
