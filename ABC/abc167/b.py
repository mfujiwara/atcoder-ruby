A,B,C,K=map(int, input().split())
if K<=A:
    print(K)
elif K<=A+B:
    print(A)
else:
    print(A*2-K+B)
