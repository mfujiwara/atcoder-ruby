import collections
N=int(input())
C=collections.deque([[0]+list(map(int, input().split())) for _ in range(pow(2,N))])
while len(C)!=1:
    A=C.popleft()
    B=C.popleft()
    AB=[]
    for i in range(1,len(A)):
        AB.append(max(A[0]+B[i],B[0]+A[i]))
    C.append(AB)
print(C[0][0])
