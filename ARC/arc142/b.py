N=int(input())
for i in range(N):
    row=[0]*N
    j=0 if i%2==0 else 1
    v=i*N+1
    for _ in range(N):
        row[j]=v
        j+=2
        if j>=N:
            j=1 if i%2==0 else 0
        v+=1
    print(*row)
