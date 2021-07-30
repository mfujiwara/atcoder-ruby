N,M=map(int, input().split())
array=list(map(int, input().split()))
counts=[0]*(M+1)
for a in array:
    counts[a]+=1
    if counts[a]*2>N:
        print(a)
        exit()
print("?")
