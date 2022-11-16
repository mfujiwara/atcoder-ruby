def popcount(x):
    x = (x & 0x5555555555555555) + (x >> 1 & 0x5555555555555555)
    x = (x & 0x3333333333333333) + (x >> 2 & 0x3333333333333333)
    x = x + (x >> 4) & 0x0f0f0f0f0f0f0f0f
    x += x >> 8
    x += x >> 16
    x += x >> 32
    return x & 0x7f

N=int(input())
A=[input() for _ in range(N)]
bits=[]
for array in A:
    tmp=[int(array[j:j+63],base=2) for j in range(0,N,63)]
    bits.append(tmp)
#print(A)
L=len(bits[0])
ret=0
for i in range(N-1):
    for j in range(i+1,N):
        if A[i][j]=="1":
            for k in range(L):
                ret+=popcount(bits[i][k]&bits[j][k])
print(ret//3)
