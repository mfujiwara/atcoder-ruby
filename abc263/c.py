import itertools
N,M=map(int, input().split())
array=[i+1 for i in range(M)]
for perm in itertools.combinations(array,N):
    print(*perm)
