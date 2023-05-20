N,M=map(int, input().split())
a_array=list(map(int, input().split()))
b_array=list(map(int, input().split()))
ret=[]
a_i=0
b_i=0
while a_i<N and b_i<M:
    if a_array[a_i]==b_array[b_i]:
        a_i+=1
        b_i+=1
    elif a_array[a_i]>b_array[b_i]:
        ret.append(b_array[b_i])
        b_i+=1
    else:
        ret.append(a_array[a_i])
        a_i+=1
if a_i==N:
    ret+=b_array[b_i:]
if b_i==M:
    ret+=a_array[a_i:]
print(" ".join(map(str,ret)))
