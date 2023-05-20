import collections
N=int(input())
array=list(map(int, input().split()))
counts=collections.defaultdict(int)
for a in array:
    counts[a]+=1
keys = list(counts.keys())
keys.sort()
if len(keys)>3:
    print("No")
elif len(keys)==3:
    if (keys[0] ^ keys[1] == keys[2]) and counts[keys[0]]==counts[keys[1]]==counts[keys[2]]:
        print("Yes")
    else:
        print("No")
elif len(keys)==2:
    if keys[0]==0 and counts[keys[0]]*2==counts[keys[1]]:
        print("Yes")
    else:
        print("No")
else:
    if keys[0]==0:
        print("Yes")
    else:
        print("No")
