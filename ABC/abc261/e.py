N,C=map(int, input().split())
array0=[0]
array1=[pow(2,30)-1]
for _ in range(N):
    t,a=map(int, input().split())
    if t==1:
        array0.append(array0[-1]&a)
        array1.append(array1[-1]&a)
    elif t==2:
        array0.append(array0[-1]|a)
        array1.append(array1[-1]|a)
    else:
        array0.append(array0[-1]^a)
        array1.append(array1[-1]^a)
for i in range(1,N+1):
    ret=0
    bit=1
    for k in range(30):
        if C&bit==0:
            ret+=array0[i]&bit
        else:
            ret+=array1[i]&bit
        bit=bit<<1
    print(ret)
    C=ret
# print(array0)
# print(array1)
