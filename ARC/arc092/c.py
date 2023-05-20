INF=pow(10,20)
N=int(input())
array=list(map(int, input().split()))
even_total=0
even_s=N
even_t=-1
even_count=0
even_dels=[]
odd_total=0
odd_s=N
odd_t=-1
odd_count=0
odd_dels=[]
for i,a in enumerate(array):
    if i%2==0:
        if a>0:
            even_total+=a
            even_s=min(even_s,i)
            even_t=max(even_t,i)
            even_count+=1
        else:
            even_dels.append(i)
    else:
        if a>0:
            odd_total+=a
            odd_s=min(odd_s,i)
            odd_t=max(odd_t,i)
            odd_count+=1
        else:
            odd_dels.append(i)
if even_total==odd_total==0:
    a,index=max([(a,i) for i,a in enumerate(array)])
    print(a)
    print(N-1)
    for i in range(N-1-index):
        print(N-i)
    for i in range(index):
        print(1)
    exit()
if even_total>odd_total:
    total=even_total
    s=even_s
    t=even_t
    count=even_count
    dels=even_dels
else:
    total=odd_total
    s=odd_s
    t=odd_t
    count=odd_count
    dels=odd_dels
print(total)
rets=[]
for i in range(N-1-t):
    rets.append(N-i)
for d in dels[::-1]:
    if s<=d<=t:
        rets.append(d+1)
for _ in range(s):
    rets.append(1)
for _ in range(count-1):
    rets.append(2)
print(len(rets))
print(*rets,sep="\n")
