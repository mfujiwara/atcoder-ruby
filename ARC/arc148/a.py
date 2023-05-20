import math
N=int(input())
array=list(set(map(int, input().split())))
if len(array)==1:
    print(1)
    exit()
diffs=[]
for i in range(len(array)-1):
    diffs.append(abs(array[i]-array[i+1]))
if len(diffs)==1:
    if diffs[0]==1:
        print(2)
    else:
        print(1)
    exit()
g=diffs[0]
for i in range(1,len(diffs)):
    g=math.gcd(g,diffs[i])
if g>1:
    print(1)
else:
    print(2)
