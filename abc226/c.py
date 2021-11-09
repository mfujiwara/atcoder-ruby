INF=pow(10,10)
N=int(input())
TKA=[]
for i in range(N):
    array=list(map(int, input().split()))
    TKA.append(array)
ret=TKA[-1][0]
targets=TKA[-1][2:]
done=[False]*N
while targets:
    t=targets.pop()
    t-=1
    if done[t]:
        continue
    ret+=TKA[t][0]
    done[t]=True
    targets+=TKA[t][2:]        
print(ret)
