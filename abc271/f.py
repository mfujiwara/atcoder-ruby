import collections
import itertools


N=int(input())
A=[list(map(int, input().split())) for _ in range(N)]
memo=collections.defaultdict(lambda: collections.defaultdict(int))
memo[(0,0)][0]=1
for i in range(N-1):
    for j in range(N-1-i):
        for k,v in memo[(i,j)].items():
            memo[(i+1,j)][k^A[i][j]]+=v
            memo[(i,j+1)][k^A[i][j]]+=v
# for i in range(N):
#     print("memo[(i,N-1-i)]",memo[(i,N-1-i)])
memo2=collections.defaultdict(lambda: collections.defaultdict(int))
memo2[(N-1,N-1)][0]=1
for i in range(N-1,0,-1):
    for j in range(N-1,N-1-i,-1):
        for k,v in memo2[(i,j)].items():
            memo2[(i-1,j)][k^A[i][j]]+=v
            memo2[(i,j-1)][k^A[i][j]]+=v
# for i in range(N):
#     print("memo2[(i,N-1-i)]",memo2[(i,N-1-i)])
ret=0
for i in range(N):
    for k,v in memo[(i,N-1-i)].items():
        k^=A[i][N-1-i]
        ret+=v*memo2[(i,N-1-i)][k]
print(ret)
