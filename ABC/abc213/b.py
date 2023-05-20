N=int(input())
array=list(map(int, input().split()))
pairs=[]
for i,a in enumerate(array):
    pairs.append((a,i))
pairs.sort()
print(pairs[-2][1]+1)
