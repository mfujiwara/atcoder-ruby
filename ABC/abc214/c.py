N=int(input())
S=list(map(int, input().split()))
T=list(map(int, input().split()))
for i in range(N):
    T[i]=min(T[i],T[(i+N-1)%N]+S[(i+N-1)%N])
for i in range(N):
    T[i]=min(T[i],T[(i+N-1)%N]+S[(i+N-1)%N])
for t in T:
    print(t)
