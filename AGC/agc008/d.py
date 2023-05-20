N=int(input())
array=list(map(int, input().split()))
array=[(a-1,i+1) for i,a in enumerate(array)]
array.sort()
rets=[0]*(N*N)
space_index=0
stock=[]
for index,a in array:
    rets[index]=a
    pre_count=a-1
    post_count=N-a
    while pre_count>0:
        if rets[space_index]==0:
            rets[space_index]=a
            space_index+=1
            pre_count-=1
        elif rets[space_index]==a:
            print("No")
            exit()
        else:
            space_index+=1
    if post_count>0:
        stock.append([a,post_count])
space_index=N*N-1
while stock:
    #print(stock,rets)
    if rets[space_index]==0:
        rets[space_index]=stock[-1][0]
        space_index-=1
        stock[-1][1]-=1
        if stock[-1][1]==0:
            stock.pop()
    elif rets[space_index]==stock[-1][0]:
        print("No")
        exit()
    else:
        space_index-=1
print("Yes")
print(*rets)
