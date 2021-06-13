import bisect
N=int(input())
if N==1:
    print(1)
    print(1)
    exit()
fib=[0]*90
fib[0]=1
fib[1]=1
for i in range(2,90):
    fib[i]=fib[i-1]+fib[i-2]
idx=bisect.bisect_left(fib,N)
if fib[idx]==N:
    print(idx+1)
    print(1)
    print(2)
    if idx%2==0:
        for i in range(idx-1):
            if i%2==0:
                print(3)
            else:
                print(4)
    else:
        for i in range(idx-1):
            if i%2==0:
                print(4)
            else:
                print(3)
    exit()
diff=N-fib[idx-1]
cnt=1
ope_cnt=0
plus=[0]*(idx-1)
plus[1]=1
def calc(plus):
    vx=1
    vy=1
    if idx%2==0:
        for i in range(idx-2):
            if i%2==0:
                for _ in range(plus[i]):
                    vx+=1
                vy+=vx
            else:
                for _ in range(plus[i]):
                    vy+=1
                vx+=vy
    else:
        for i in range(idx-2):
            if i%2==0:
                for _ in range(plus[i]):
                    vy+=1
                vx+=vy
            else:
                for _ in range(plus[i]):
                    vx+=1
                vy+=vx
    return vx
for i in range(2,idx-1):
    v=calc(plus)
    if v==N:
        break
    if v>N:
        plus[i-1]-=1
        plus[i]+=1
    else:
        plus[i]+=1
print(idx+plus.count(1))
print(1)
print(2)
vx=1
vy=1
if idx%2==0:
    for i in range(idx-2):
        if i%2==0:
            for j in range(plus[i]):
                print(1)
                vx+=1
            print(4)
            vy+=vx
        else:
            for j in range(plus[i]):
                print(2)
                vy+=1
            print(3)
            vx+=vy
else:
    for i in range(idx-2):
        if i%2==0:
            for j in range(plus[i]):
                print(2)
                vy+=1
            print(3)
            vx+=vy
        else:
            for j in range(plus[i]):
                print(1)
                vx+=1
            print(4)
            vy+=vx
