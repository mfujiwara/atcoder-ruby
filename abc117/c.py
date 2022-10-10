N,M=map(int, input().split())
array=list(map(int, input().split()))
if N>=M:
    print(0)
    exit()
array.sort()
diffs=[]
for i in range(M-1):
    diffs.append(array[i+1]-array[i])
diffs.sort()
print(sum(diffs[:M-N]))
#print(diffs)
