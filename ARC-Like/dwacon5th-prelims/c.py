N=int(input())
S=input()
s_array=[]
for ch in S:
    if ch=="D":
        s_array.append(0)
    elif ch=="M":
        s_array.append(1)
    elif ch=="C":
        s_array.append(2)
    else:
        s_array.append(3)
Q=int(input())
k_array=list(map(int, input().split()))
for k in k_array:
    dd=0
    mm=0
    dm=0
    ret=0
    for i,s in enumerate(s_array):
        if i>=k:
            if s_array[i-k]==0:
                dd-=1
                dm-=mm
            elif s_array[i-k]==1:
                mm-=1
        if s==0:
            dd+=1
        elif s==1:
            mm+=1
            dm+=dd
        elif s==2:
            ret+=dm
    print(ret)
