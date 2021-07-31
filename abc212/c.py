N,M=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
a_array.sort()
b_array.sort()
ret=1<<60
i=j=0
while True:
    v=a_array[i]-b_array[j]
    ret=min(ret,abs(v))
    if ret==0:
        break
    if i==N-1 and j==M-1:
        break
    if i==N-1:
        j+=1
    elif j==M-1:
        i+=1
    elif v>0:
        j+=1
    else:
        i+=1
print(ret)
