K=int(input())
i=pow(10,16)-1
mini=(i,sum(list(map(int,list(str(i))))))
rets=[i]
while mini[0]!=1:
    i-=max(1,pow(10,len(str(i))-4))
    v=(i,sum(list(map(int,list(str(i))))))
    if v[0]*mini[1]<=mini[0]*v[1]:
        rets.append(v[0])
        mini=v
rets=rets[::-1]
for i in range(K):
    print(rets[i])
