N,K=map(int, input().split())
array=[]
for _ in range(N):
    a,b=map(int, input().split())
    array.append(b)
    array.append(a-b)
array.sort(reverse=True)
print(sum(array[:K]))
