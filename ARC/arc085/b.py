N,Z,W=map(int, input().split())
array=list(map(int, input().split()))
if N==1:
    print(abs(array[0]-W))
else:
    v=max(abs(array[-1]-array[-2]),abs(array[-1]-W))
    print(v)
