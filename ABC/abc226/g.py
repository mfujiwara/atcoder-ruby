T=int(input())
for _ in range(T):
    a_array=list(map(int, input().split()))
    b_array=list(map(int, input().split()))
    for i in range(5):
        mini=min(a_array[i],b_array[i])
        a_array[i]-=mini
        b_array[i]-=mini
    #print(a_array,b_array)
    if a_array[4]>0:
        print("No")
        continue
    if b_array[4]>0 and a_array[3]>0:
        mini=min(b_array[4],a_array[3])
        b_array[4]-=mini
        a_array[3]-=mini
        b_array[0]+=mini
    #print(a_array,b_array)
    if a_array[3]>0:
        print("No")
        continue
    for n in range(4,2,-1):
        if b_array[n]>0 and a_array[2]>0:
            mini=min(b_array[n],a_array[2])
            b_array[n]-=mini
            a_array[2]-=mini
            b_array[n-3]+=mini
    #print(a_array,b_array)
    if a_array[2]>0:
        print("No")
        continue
    for n in range(4,0,-1):
        if b_array[n]>0 and a_array[1]>0:
            mini=min(b_array[n],a_array[1])
            b_array[n]-=mini
            a_array[1]-=mini
            if n-2>=0:
                b_array[n-2]+=mini
    #print(a_array,b_array)
    if a_array[1]>0:
        print("No")
        continue
    for n in range(4,-1,-1):
        if b_array[n]>0 and a_array[0]>0:
            mini=min(b_array[n],a_array[0])
            b_array[n]-=mini
            a_array[0]-=mini
            if n-1>=0:
                b_array[n-1]+=mini
    #print(a_array,b_array)
    if a_array[0]>0:
        print("No")
        continue
    print("Yes")
