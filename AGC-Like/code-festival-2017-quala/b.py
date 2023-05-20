N,M,K=map(int, input().split())
for i in range(N+1):
    for j in range(M+1):
        if K==M*i+N*j-i*j*2:
            print("Yes")
            exit()
print("No")
