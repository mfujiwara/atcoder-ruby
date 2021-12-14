import bisect
N,Q=map(int, input().split())
array=list(map(int, input().split()))
array.sort()
for _ in range(Q):
    x=int(input())
    print(N-bisect.bisect_left(array,x))
