import math
INF=pow(10,20)
N=int(input())
array=list(map(int, input().split()))
array=[math.log2(a) for a in array]
# minus[i]:=先頭からi個を負の数で昇順にするために必要な操作回数
minus=[0]*(N+1)
# plus[i]:=末尾からi個を負の数で昇順にするために必要な操作回数
plus=[0]*(N+1)
stack=[(INF,INF,1)]
count=0
for i in range(N):
    a=array[i]+1
    count+=1
    val=(a,a,1)
    while stack[-1][0]<val[1]:
        b0,b1,c=stack.pop()
        t0=int((val[1]-b0)//2)*2
        if b0+t0<val[1]:
            t0+=2
        count+=t0*c
        val=(val[0],b1+t0,c+val[2])
    stack.append(val)
    minus[i+1]=count
    #print(stack)
stack=[(INF,INF,1)]
count=0
for i in range(N):
    a=array[N-1-i]
    val=(a,a,1)
    while stack[-1][0]<val[1]:
        b0,b1,c=stack.pop()
        t0=int((val[1]-b0)//2)*2
        if b0+t0<val[1]:
            t0+=2
        count+=t0*c
        val=(val[0],b1+t0,c+val[2])
    stack.append(val)
    plus[i+1]=count
    #print(stack)
ret=INF
for i in range(N+1):
    ret=min(ret,minus[i]+plus[N-i])
print(ret)
# print(minus)
# print(plus)
# print(array)
