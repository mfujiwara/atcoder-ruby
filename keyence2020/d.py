import collections
INF=400
N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
if N==1:
    print(0)
    exit()
ret=INF
for bit in range(pow(2,N-1)):
    nums=[]
    counts=collections.defaultdict(list)
    b_count=0
    for i in range(N-1):
        bit,r=divmod(bit,2)
        if r==1:
            nums.append(B[i])
            counts[(B[i],(i+1)%2)].append(i)
            b_count+=1
        else:
            nums.append(A[i])
            counts[(A[i],i%2)].append(i)
    if b_count%2==0:
        nums.append(A[N-1])
        counts[(A[N-1],(N-1)%2)].append(N-1)
    else:
        nums.append(B[N-1])
        counts[(B[N-1],N%2)].append(N-1)
    nums.sort()
    valid=True
    d=0
    ddd=[i for i in range(N)]
    for i,n in enumerate(nums):
        if len(counts[(n,i%2)])==0:
            valid=False
            break
        k=counts[(n,i%2)].pop(0)
        j=ddd.index(k)
        ddd.pop(j)
        d+=j
    if valid:
        ret=min(ret,d)
if ret==INF:
    print(-1)
else:
    print(ret)
