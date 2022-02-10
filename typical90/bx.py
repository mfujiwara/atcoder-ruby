N=int(input())
array=list(map(int, input().split()))
total=sum(array)
if total%10!=0:
    print("No")
    exit()
target=total//10
start=0
s=0
i=0
while True:
    s+=array[i]
    while s>target:
        s-=array[start]
        start+=1
        if start==N:
            print("No")
            exit()
    if s==target:
        print("Yes")
        exit()
    i+=1
    i%=N
