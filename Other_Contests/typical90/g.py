import bisect
N=int(input())
array=sorted(list(map(int, input().split())))
Q=int(input())
for _ in range(Q):
    b=int(input())
    i=bisect.bisect_right(array,b)
    if i==0:
        print(abs(array[0]-b))
    elif i==N:
        print(abs(array[-1]-b))
    else:
        r1=abs(array[i]-b)
        r2=abs(array[i-1]-b)
        print(min(r1,r2))
