N=int(input())
array=list(map(int, input().split()))
sums1=[array[0]]
sums2=[array[1]]
for i in range(2,N):
    if i%2==0:
        sums1.append(sums1[-1]+array[i])
    else:
        sums2.append(sums2[-1]+array[i])
if N%2==0:
    ret=sums2[-1]
    for i in range(N//2):
        r=sums1[i]+sums2[-1]-sums2[i]
        ret=max(ret,r)
    print(ret)
else:
    ret=sums1[-1]-sums1[0]
    brray=[]
    for i in range(N//2):
        r=sums2[i]+sums1[-1]-sums1[i+1]
        ret=max(ret,r)
        brray.append((r,i))
    brray.sort()
    _,j=brray.pop()
    for i in range(N//2):
        while j<i and brray:
            _,j=brray.pop()
        r=sums1[i]+sums2[j]-sums2[i]+sums1[-1]-sums1[j+1]
        ret=max(ret,r)
    print(ret)
