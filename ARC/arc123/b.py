from sys import argv


N=int(input())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
c_array=list(map(int, input().split()))
a_array.sort()
b_array.sort()
c_array.sort()
b_index=0
c_index=0
ret=0
for a in a_array:
    if b_index>=N or c_index>=N:
        break
    b=b_array[b_index]
    while b<=a and b_index<N-1:
        b_index+=1
        b=b_array[b_index]
    if b<=a:
        break
    b_index+=1

    c=c_array[c_index]
    while c<=b and c_index<N-1:
        c_index+=1
        c=c_array[c_index]
    if c<=b:
        break
    c_index+=1
    ret+=1
print(ret)
