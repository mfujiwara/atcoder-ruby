import bisect
import collections
INF=pow(10,10)
N=int(input())
uu_array=collections.defaultdict(list) #1
dd_array=collections.defaultdict(list) #1
ld_array=collections.defaultdict(list) #2
ru_array=collections.defaultdict(list) #2

#uu_array=collections.defaultdict(list) #1
#ru_array=collections.defaultdict(list) #2
du_array=collections.defaultdict(list) #3
lu_array=collections.defaultdict(list) #4
ur_slash=collections.defaultdict(list) #4
rr_slash=collections.defaultdict(list) #1
dr_slash=collections.defaultdict(list) #2
lr_slash=collections.defaultdict(list) #3

for _ in range(N):
    x,y,u=input().split()
    x=int(x)
    y=int(y)
    if u=="U":
        uu_array[x].append(y) #1
        ur_slash[y-x].append(-x) #4
    elif u=="R":
        rr_slash[x+y].append(y) #1
        ru_array[-y].append(x) #2
    elif u=="D":
        dd_array[x].append(y) #1
        dr_slash[x-y].append(x) #2
        du_array[-x].append(-y) #3
    else:
        ld_array[-y].append(x) #2
        lu_array[y].append(-x) #4
        lr_slash[-x-y].append(-y) #3
ret=INF
for array in [uu_array,dd_array,ld_array,ru_array,du_array,lu_array,ur_slash,rr_slash,dr_slash,lr_slash]:
    for a in array.keys():
        array[a]=sorted(array[a])
for uu,dd in [(uu_array,dd_array),(ru_array,ld_array)]:
    for x in uu:
        for y in uu[x]:
            ind=bisect.bisect_right(dd[x],y)
            if ind<len(dd[x]):
                ret=min(ret,abs(dd[x][ind]-y)*5)
for i,uurr in enumerate([(uu_array,rr_slash),(ru_array,dr_slash),(du_array,lr_slash),(lu_array,ur_slash)]):
    uu,rr=uurr
    for x in uu:
        for y in uu[x]:
            ind=bisect.bisect_right(rr[x+y],y)
            if ind<len(rr[x+y]):
                ret=min(ret,abs(rr[x+y][ind]-y)*10)
if ret!=INF:
    print(ret)
else:
    print("SAFE")
