N=int(input())
if bin(N).count("1")==1:
    print("No")
    exit()

print("Yes")
print(1,2)
print(2,3)
print(3,N+1)
print(N+1,N+2)
print(N+2,N+3)

for i in range(4,N,2):
    print(i,i+1)
    print(i+1,N+1)
    print(N+1,N+i)
    print(N+i,N+i+1)

if N%2==0:
    print(N,N-1)
    x=N^(N-1)^1
    print(N+x,2*N)
