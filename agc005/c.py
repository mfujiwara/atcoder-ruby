import collections
N=int(input())
array=list(map(int, input().split()))
counts=collections.defaultdict(int)
for a in array:
    counts[a]+=1
keys=list(counts.keys())
mini=min(keys)
maxi=max(keys)
first=True
for key in range(mini,maxi+1):
    c=counts[key]
    if first:
        first=False
        if c==1:
            if maxi!=mini*2:
                print("Impossible")
                exit()
        elif c==2:
            if maxi!=mini*2-1:
                print("Impossible")
                exit()
        else:
            print("Impossible")
            exit()
    else:
        if c<2:
            print("Impossible")
            exit()
print("Possible")
