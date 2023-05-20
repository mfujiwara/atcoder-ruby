N,K=map(int, input().split())
sum_ab=(K+K+2*N-1)*2*N//2
sum_c=(K+2*N+K+3*N-1)*N//2
# 2*(3K+2N-1)>4K+5N-1
# 2K-1>N
if sum_ab>sum_c: 
    print(-1)
    exit()
a_array=[]
b_array1=[]
b_array2=[]
a=K
b=K+2*N-1
b_array=b_array2
for i in range(N):
    if a>=K+N:
        a=K+1
        b_array=b_array1
    a_array.append(a)
    b_array.append(b)
    a+=2
    b-=1
if len(b_array1)!=len(b_array2):
    b=b_array2.pop()
    b_array1=[b]+b_array1
b_array=b_array1+b_array2
for i in range(N):
    print(a_array[i],b_array[i],K+2*N+i)
