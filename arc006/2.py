N,L=map(int, input().split())
array=[i for i in range(N)]
for _ in range(L):
    x=input()
    for i in range(N-1):
        ch=x[i*2+1]
        if ch=="-":
            array[i],array[i+1]=array[i+1],array[i]
y=input()
for i in range(N):
    ch=y[i*2]
    if ch=="o":
        print(array[i]+1)
