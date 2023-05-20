N,M=map(int, input().split())
a_array=list(map(int, input().split()))
c_array=list(map(int, input().split()))
b_array=[0]*(M+1)
for i in range(M,-1,-1):
    # i+N次の係数
    base=0
    for j in range(i+1,M+1):
        base+=b_array[j]*a_array[i+N-j]
        if i+N==j:
            break
    # base+b*a_array[N]=c_array[i+N]
    b=(c_array[i+N]-base)//a_array[N]
    b_array[i]=b
print(*b_array)
