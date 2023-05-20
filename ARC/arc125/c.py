import collections
N,K=map(int, input().split())
array=collections.deque(map(int, input().split()))
done=[False]*(N+1)
rets=[]
i=1
while True:
    if done[i]:
        i+=1
        continue
    if len(array)==1:
        break
    a=array.popleft()
    rets.append(a)
    done[a]=True
    if i<a:
        rets.append(i)
        done[i]=True
        i+=1
rets+=[i for i in range(N,i-1,-1) if done[i]==False]
print(*rets)
