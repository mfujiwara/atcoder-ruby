H,W,h,w=map(int, input().split())
if W%w!=0:
    sums=[0]
    for i in range(1,W+1):
        if W%w==i%w:
            v=(W-i)//w+1
            sums.append(v)
        elif len(sums)>=w:
            sums.append(sums[-w]-1)
        else:
            sums.append(sums[-1]+1)
    array=[]
    for i in range(len(sums)-1):
        array.append(sums[i+1]-sums[i])
    print("Yes")
    for _ in range(H):
        print(*array)
elif H%h!=0:
    sums=[0]
    for i in range(1,H+1):
        if H%h==i%h:
            v=(H-i)//h+1
            sums.append(v)
        elif len(sums)>=h:
            sums.append(sums[-h]-1)
        else:
            sums.append(sums[-1]+1)
    array=[]
    for i in range(len(sums)-1):
        array.append(sums[i+1]-sums[i])
    print("Yes")
    for a in array:
        print(*[a]*W)
else:
    print("No")
