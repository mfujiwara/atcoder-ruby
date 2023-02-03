N,K=map(int, input().split())
array=list(map(int, input().split()))
print(sum(sorted(array)[:K]))
