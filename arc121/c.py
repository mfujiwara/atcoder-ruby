T=int(input())
for t in range(T):
    #print("====t",t)
    N=int(input())
    array=list(map(int, input().split()))
    if N==2:
        if array==[1,2]:
            print(0)
            print()
        else:
            print(1)
            print(1)
        continue
    rets=[]
    if len(array)>4:
        for i in range(N,4,-1):
            k=array.index(i)
            if len(rets)%2!=k%2 and k!=i-1:
                if k>2:
                    if len(rets)%2==0:
                        rets.append(1)
                        array[0],array[1]=array[1],array[0]
                    else:
                        rets.append(2)
                        array[2],array[1]=array[1],array[2]
                else:
                    if len(rets)%2==len(array)%2:
                        rets.append(len(array)-1)
                        array[-1],array[-2]=array[-2],array[-1]
                    else:
                        rets.append(len(array)-2)
                        array[-3],array[-2]=array[-2],array[-3]
            rets+=[j for j in range(k+1,i)]
            array.pop(k)
    if len(array)==4:
        if array[0]==4:
            if len(rets)%2==0:
                rets.append(1)
                array[0],array[1]=array[1],array[0]
            else:
                rets.append(2)
                rets.append(1)
                array[0],array[1],array[2]=array[2],array[0],array[1]
        if array[3]!=4 and len(rets)%2==0:
            rets.append(3)
            array[2],array[3]=array[3],array[2]
        while array[3]!=4:
            rets.append(2)
            rets.append(3)
            array[1],array[2],array[3]=array[2],array[3],array[1]
        array.pop()
    while array!=[1,2,3]:
        if len(rets)%2==0:
            rets.append(1)
            array[0],array[1]=array[1],array[0]
        else:
            rets.append(2)
            array[2],array[1]=array[1],array[2]
    print(len(rets))
    print(*rets)
