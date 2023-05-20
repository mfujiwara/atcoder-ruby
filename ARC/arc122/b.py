def calc(array,x):
    total=0
    for a in array:
        v=x+a-min(a,2*x)
        total+=v
    return total/len(array)
N=int(input())
array=list(map(int, input().split()))
left=0
right=10**9
while True:
    if right-left<pow(10,-7):
        print(calc(array,right))
        exit()
    c1=(left*2+right)/3
    c2=(left+right*2)/3
    v1=calc(array,c1)
    v2=calc(array,c2)
    if v1<v2:
        right=c2
    elif v2<v1:
        left=c1
    else:
        left=c1
        right=c2
