N=int(input())
array=list(map(int, input().split()))
mini_i=0
for i,a in enumerate(array):
    if a<array[mini_i]:
        mini_i=i
array=array[mini_i:]+array[:mini_i]
#print(array)
ret=array[0]
if ret>0:
    maxi=0
    for i in range(N):
        if array[i]<=maxi:
            break
        array[i]=max(array[i]-ret,maxi)
        maxi=max(maxi,array[i])
    #print(array,i)
    j=i
    maxi=0
    for i in range(N-1,j-1,-1):
        #print(i)
        if array[i]<=maxi:
            break
        array[i]=max(array[i]-ret,maxi)
        maxi=max(maxi,array[i])
    #print(array)
for i in range(N-1):
    ret+=max(0,array[i+1]-array[i])
print(ret)
