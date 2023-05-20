N,X=map(int, input().split())
array=list(map(int, input().split()))
done=[False]*N
x=X-1
ret=0
while not done[x]:
    ret+=1
    done[x]=True
    x=array[x]-1
print(ret)
