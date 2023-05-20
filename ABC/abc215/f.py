import collections
N=int(input())
x2y=collections.defaultdict(list)
for _ in range(N):
    x,y=map(int, input().split())
    x2y[x].append(y)
x_array=sorted(list(x2y.keys()))
if len(x_array)==1:
    print(0)
    exit()
minmax_left=[]
minmax_right=[]
for x in x_array:
    mini=min(x2y[x])
    maxi=max(x2y[x])
    if len(minmax_left)>0:
        mini=min(mini,minmax_left[-1][0])
        maxi=max(maxi,minmax_left[-1][1])
    minmax_left.append((mini,maxi))
for x in x_array[::-1]:
    mini=min(x2y[x])
    maxi=max(x2y[x])
    if len(minmax_right)>0:
        mini=min(mini,minmax_right[-1][0])
        maxi=max(maxi,minmax_right[-1][1])
    minmax_right.append((mini,maxi))
minmax_right=minmax_right[::-1]
left=0
right=pow(10,9)+1
while True:
    if left+1==right:
        print(left)
        exit()
    mid=(left+right)//2
    valid=False
    ri=1
    for i,x in enumerate(x_array):
        while ri<len(x_array) and x+mid>x_array[ri]:
            ri+=1
        if ri==len(x_array): break
        if minmax_left[i][1]-minmax_right[ri][0]>=mid or minmax_right[ri][1]-minmax_left[i][0]>=mid:
            valid=True
            break
    if valid:
        left=mid
    else:
        right=mid
