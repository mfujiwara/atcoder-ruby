import collections
N=int(input())
array=list(map(int, input().split()))
ret=0
b_array=[0]
c_array=[0]
for a in array:
    diff=a-b_array[-1]-c_array[-1]
    if diff>0:
        b_array.append(b_array[-1]+diff)
        c_array.append(c_array[-1])
    else:
        b_array.append(b_array[-1])
        c_array.append(c_array[-1]+diff)
bc_array=sorted(b_array+list(map(lambda e: -e,c_array)),reverse=True)
now=sum(bc_array)
ret=now
while bc_array and bc_array[-1]==0:
    bc_array.pop()
pre_v=0
while bc_array:
    v=bc_array.pop()
    count=1
    while bc_array and bc_array[-1]==v:
        bc_array.pop()
        count+=1
    v_diff=v-pre_v
    now+=(N-len(bc_array)-count)*v_diff*2
    pre_v=v
    ret=min(ret,now)
print(ret)

