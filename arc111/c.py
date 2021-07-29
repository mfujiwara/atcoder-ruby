N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
p_array=list(map(int, input().split()))
ais=[] # (i,a) 人iの体重はa
bags=[] # bags[i]=(p,b) 人iが重さbの荷物pを持っている
for i in range(N):
    a=a_array[i]
    ais.append((i,a))

    p=p_array[i]-1
    b=b_array[p]
    bags.append((p,b))
    if i!=p and a<=b:
        print(-1)
        exit()
ais.sort(key=lambda e: -e[1])
rets=[]
for i,a in ais:
    p,b=bags[i]
    while p!=i:
        rets.append((i,p))
        bags[i],bags[p]=bags[p],bags[i]
        p,b=bags[i]
print(len(rets))
for i,p in rets:
    print(f"{i+1} {p+1}")
