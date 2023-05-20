N=int(input())
array=list(map(int, input().split()))
sorted_array=sorted([(a,i) for i,a in enumerate(array)])
mid=sorted_array[N//2][0]
#print("mid",mid)
S=sum(map(lambda e: e[0],sorted_array[N//2:]))
mini=(0,0)
now=0
for i,a in enumerate(array):
    if mid<=a:
        now-=1
    else:
        now+=1
    mini=min(mini,(now,i+1))
    #print((now,i+1))
print(mini[1]%N,S)
